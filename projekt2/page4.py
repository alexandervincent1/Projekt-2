import os
import threading
import json
import joblib
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from gpt4all import GPT4All

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
META_PATH = MODEL_PATH + ".meta.json"
DEFAULT_CSV = os.path.join(BASE_DIR, "test.csv")
LOCAL_GPT_MODEL = r"C:\Users\eric.rocklind\Documents\AI\gpt4all-falcon-newbpe-q4_0.gguf"

def try_load_model_from_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return joblib.load(path)

class Page4(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor, collection=None):
        super().__init__(parent, bg=backgroundcolor)
        self.collection = collection
        self.model = None
        self.feature_columns = []
        self._build_ui()

    def _build_ui(self):
        # --- White content box ---
        content = tk.Frame(self, bg="white", bd=2, relief="groove")
        content.pack(padx=20, pady=20, fill="both")

        # --- Header ---
        tk.Label(
            content,
            text="AI — Träna & Prediktera",
            bg="white",
            font=("Arial", 18)
        ).pack(pady=15)

        # --- Buttons row ---
        btn_frame = tk.Frame(content, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Träna (test.csv)", command=self.train).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Ladda modell", command=self.load_model).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Kör AI (prediktera)", command=self.predict).pack(side="left", padx=10)
        # --- Input form ---
        form = tk.Frame(content, bg="white")
        form.pack(pady=20)

        # Statusrad för att visa meddelanden från metoderna
        self.status = tk.Label(content, text="", bg="white", fg="green", font=("Arial", 11), justify="left", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(5,15))

        tk.Label(form, text="Datum (YYYY-MM-DD):", bg="white", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.e_datum = tk.Entry(form, font=("Arial", 12))
        self.e_datum.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form, text="Maträtt:", bg="white", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.e_meal = tk.Entry(form, font=("Arial", 12))
        self.e_meal.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form, text="Elever närvarande:", bg="white", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        self.e_total = tk.Entry(form, font=("Arial", 12))
        self.e_total.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form, text="Elever som åt:", bg="white", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
        self.e_ate = tk.Entry(form, font=("Arial", 12))
        self.e_ate.grid(row=3, column=1, padx=10, pady=5)


    def set_status(self, txt):
        self.status.config(text=txt)

    def train(self):
        csv_path = DEFAULT_CSV if os.path.exists(DEFAULT_CSV) else filedialog.askopenfilename(filetypes=[("CSV","*.csv")])
        if not csv_path:
            self.set_status("Ingen CSV vald.")
            return
        self.set_status("Tränar modellen...")
        threading.Thread(target=self._train_bg, args=(csv_path,), daemon=True).start()

    def _train_bg(self, csv_path):
        try:
            df = pd.read_csv(csv_path)
            if "mat_slängt_kg" in df.columns:
                y_col = "mat_slängt_kg"
            elif "food_waste_kg" in df.columns:
                y_col = "food_waste_kg"
            else:
                self.after(0, lambda: self.set_status("Ingen målkolumn i CSV. Använd mat_slängt_kg eller food_waste_kg."))
                return

            for c in ("students_total", "students_ate"):
                df[c] = pd.to_numeric(df.get(c, 0), errors="coerce").fillna(0)

            X = pd.get_dummies(df[["students_total", "students_ate", "meal"]].fillna(""), columns=["meal"], dummy_na=False)
            y = pd.to_numeric(df[y_col], errors="coerce").fillna(0)

            model = RandomForestRegressor(n_estimators=100, random_state=0)
            model.fit(X, y)

            joblib.dump(model, MODEL_PATH)
            with open(META_PATH, "w", encoding="utf-8") as fh:
                json.dump({"feature_columns": X.columns.tolist()}, fh, ensure_ascii=False)

            self.model = model
            self.feature_columns = X.columns.tolist()
            self.after(0, lambda: self.set_status("Träning klar. model.pkl skapad."))
        except Exception as e:
            self.after(0, lambda: self.set_status(f"Träning misslyckades: {e}"))

    def load_model(self):
        try:
            self.model = try_load_model_from_file(MODEL_PATH)
            if os.path.exists(META_PATH):
                with open(META_PATH, "r", encoding="utf-8") as fh:
                    meta = json.load(fh)
                self.feature_columns = meta.get("feature_columns", [])
            self.set_status("Modell inläst.")
        except Exception as e:
            self.set_status(f"Kunde inte läsa modell: {e}")

    def predict(self):
        try:
            row = {
                "datum": self.e_datum.get(),
                "meal": self.e_meal.get(),
                "students_total": float(self.e_total.get()),
                "students_ate": float(self.e_ate.get())
            }
        except Exception as e:
            self.set_status(f"Fel i inmatning: {e}")
            return
        self.set_status("Predikterar...")
        threading.Thread(target=self._predict_bg, args=(row,), daemon=True).start()

    def _predict_bg(self, row):
        try:
            if self.model is None:
                try:
                    self.model = try_load_model_from_file(MODEL_PATH)
                    if os.path.exists(META_PATH):
                        with open(META_PATH, "r", encoding="utf-8") as fh:
                            meta = json.load(fh)
                        self.feature_columns = meta.get("feature_columns", [])
                except Exception:
                    self.after(0, lambda: self.set_status("Ingen modell tillgänglig. Träna först."))
                    return

            df = pd.DataFrame([row])
            df["students_total"] = pd.to_numeric(df["students_total"], errors="coerce").fillna(0)
            df["students_ate"] = pd.to_numeric(df["students_ate"], errors="coerce").fillna(0)
            df["meal"] = df["meal"].fillna("")

            X = pd.get_dummies(df[["students_total", "students_ate", "meal"]], columns=["meal"], dummy_na=False)

            if self.feature_columns:
                for c in self.feature_columns:
                    if c not in X.columns:
                        X[c] = 0
                X = X[self.feature_columns]

            preds = self.model.predict(X)
            pred_val = float(np.asarray(preds).ravel()[0])

            explanation = "(GPT4All ej tillgänglig)"
            try:
                if os.path.exists(LOCAL_GPT_MODEL):
                    gpt = GPT4All(LOCAL_GPT_MODEL)
                    prompt = (
                        f"Datum: {row['datum']}\nMaträtt: {row['meal']}\n"
                        f"Totala elever: {row['students_total']}\nElever som åt: {row['students_ate']}\n\n"
                        f"Prediktion (kg): {pred_val:.2f}\nSkriv 2-3 meningar på svenska som förklarar prediktionen och ge ett enkelt råd."
                    )
                    resp = gpt.generate(prompt)
                    explanation = resp if isinstance(resp, str) else str(resp)
                else:
                    explanation = "(GPT4All-modell saknas i angiven sökväg.)"
            except Exception:
                explanation = "(Fel vid anrop till GPT4All.)"

            self.after(0, lambda: self.set_status(f"Prediktion: {pred_val:.2f} kg\n\nFörklaring:\n{explanation}"))
        except Exception as e:
            self.after(0, lambda: self.set_status(f"Prediktion misslyckades: {e}"))