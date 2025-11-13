from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox
from backend import add_entry, get_total

class Page1(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor, collection):
        super().__init__(parent, bg=backgroundcolor)
        self.collection = collection

        content_frame = tk.Frame(self, bg=backgroundcolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)

        left_box = tk.Frame(content_frame, bg=headercolor, relief="ridge", borderwidth=2)
        left_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.total_label = tk.Label(left_box, text="", bg=headercolor, font=("Arial", 16))
        self.total_label.pack(expand=True)
        self.update_total()

        right_box = tk.Frame(content_frame, bg=headercolor, relief="ridge", borderwidth=2)
        right_box.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tk.Label(right_box, text="Lägg till data", bg=headercolor, font=("Arial", 16)).pack(pady=(10, 20))

        input_frame = tk.Frame(right_box, bg=headercolor)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Datum:", bg=headercolor, font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.date_picker = DateEntry(input_frame, width=12, background='darkblue', foreground='white', borderwidth=2, state="readonly")
        self.date_picker.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Kilo mat slängts:", bg=headercolor, font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.data_entry = tk.Entry(input_frame, width=10)
        self.data_entry.grid(row=1, column=1, padx=5, pady=10)

        add_button = tk.Button(input_frame, text="Lägg till", font=("Arial", 12), command=self.add_data)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_data(self):
        date = self.date_picker.get_date()
        value = self.data_entry.get()

        if not value:
            messagebox.showwarning("Fel", "Skriv in mängden mat som slängts.")
            return

        try:
            amount = float(value)
        except ValueError:
            messagebox.showerror("Fel", "Värdet måste vara ett tal.")
            return

        add_entry(self.collection, date, amount)
        messagebox.showinfo("Data tillagd", f"Datum: {date}\nMängd: {amount} kg")

        self.update_total()
        self.data_entry.delete(0, tk.END)

    def update_total(self):
        total = get_total(self.collection)
        self.total_label.config(text=f"Totalt slängd mat: {total:.2f} kg")
