import os
import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

BASE = os.path.dirname(__file__)
CSV = os.path.join(BASE, "test.csv")
MODEL = os.path.join(BASE, "model.pkl")
META = MODEL + ".meta.json"

def main():
    df = pd.read_csv(CSV)
    # välj mål-kolumn i ditt test.csv
    if "mat_slängt_kg" in df.columns:
        y_col = "mat_slängt_kg"
    elif "food_waste_kg" in df.columns:
        y_col = "food_waste_kg"
    else:
        raise RuntimeError("Ingen målkolumn i CSV. Använd mat_slängt_kg eller food_waste_kg")

    # säkerställ numeriska kolumner
    for c in ("students_total", "students_ate"):
        df[c] = pd.to_numeric(df.get(c, 0), errors="coerce").fillna(0)

    # enkla features: students_total, students_ate och meal 
    X = pd.get_dummies(df[["students_total", "students_ate", "meal"]].fillna(""), columns=["meal"], dummy_na=False)
    y = pd.to_numeric(df[y_col], errors="coerce").fillna(0)

    print("Träningsdata shape:", X.shape)
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, y)

    joblib.dump(model, MODEL)
    with open(META, "w", encoding="utf-8") as fh:
        json.dump({"feature_columns": X.columns.tolist()}, fh, ensure_ascii=False)

    print("Träning klar. Sparat:", MODEL)
    print("Features:", X.columns.tolist())

if __name__ == "__main__":
    main()