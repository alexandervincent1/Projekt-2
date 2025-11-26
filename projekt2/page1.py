from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox
from backend import add_entry, get_total_food_waste, get_total_students_ate, get_average_food_waste_per_meal

# dashboard

class Page1(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor, collection):
        super().__init__(parent, bg=backgroundcolor)
        self.collection = collection

        content_frame = tk.Frame(self, bg=backgroundcolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)

        # --- Left Box: Total stats ---
        left_box = tk.Frame(content_frame, bg=headercolor, relief="ridge", borderwidth=2)
        left_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.total_label = tk.Label(left_box, text="", bg=headercolor, font=("Arial", 16))
        self.total_label.pack(expand=True)
        self.update_total()

        # --- Right Box: Add entry ---
        right_box = tk.Frame(content_frame, bg=headercolor, relief="ridge", borderwidth=2)
        right_box.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tk.Label(right_box, text="Lägg till data", bg=headercolor, font=("Arial", 16)).pack(pady=(10, 20))
        input_frame = tk.Frame(right_box, bg=headercolor)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Datum:", bg=headercolor).grid(row=0, column=0, sticky="e")
        self.date_picker = DateEntry(input_frame, width=12, background='darkblue', foreground='white', borderwidth=2, state="readonly")
        self.date_picker.grid(row=0, column=1)

        tk.Label(input_frame, text="Måltid:", bg=headercolor).grid(row=1, column=0, sticky="e")
        self.meal_entry = tk.Entry(input_frame)
        self.meal_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="Totala elever:", bg=headercolor).grid(row=2, column=0, sticky="e")
        self.total_students_entry = tk.Entry(input_frame)
        self.total_students_entry.grid(row=2, column=1)

        tk.Label(input_frame, text="Elever åt:", bg=headercolor).grid(row=3, column=0, sticky="e")
        self.students_ate_entry = tk.Entry(input_frame)
        self.students_ate_entry.grid(row=3, column=1)

        tk.Label(input_frame, text="Matavfall (kg):", bg=headercolor).grid(row=4, column=0, sticky="e")
        self.food_waste_entry = tk.Entry(input_frame)
        self.food_waste_entry.grid(row=4, column=1)

        add_button = tk.Button(input_frame, text="Lägg till", command=self.add_data)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_data(self):
        date = self.date_picker.get_date()
        meal = self.meal_entry.get()
        try:
            students_total = int(self.total_students_entry.get())
            students_ate = int(self.students_ate_entry.get())
            food_waste = float(self.food_waste_entry.get())
        except ValueError:
            messagebox.showerror("Fel", "Felaktig inmatning, kontrollera siffrorna.")
            return

        add_entry(self.collection, date, meal, students_total, students_ate, food_waste)
        messagebox.showinfo("Data tillagd", f"{meal} - {food_waste} kg matavfall")
        self.update_total()
        self.meal_entry.delete(0, tk.END)
        self.total_students_entry.delete(0, tk.END)
        self.students_ate_entry.delete(0, tk.END)
        self.food_waste_entry.delete(0, tk.END)

    def update_total(self):
        total_waste = get_total_food_waste(self.collection)
        avg_per_student = get_average_food_waste_per_meal(self.collection)
        self.total_label.config(
            text=f"Totalt matavfall: {total_waste:.2f} kg\n"
                 f"Genomsnittligt matavfall per elev: {avg_per_student:.2f} kg"
        )
