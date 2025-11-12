from tkcalendar import DateEntry
import tkinter as tk
from backend import get_total_on_date

class Page3(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor, collection):
        super().__init__(parent, bg=backgroundcolor)
        self.collection = collection

        content_frame = tk.Frame(self, bg=headercolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(content_frame, text="Specifik Dag", font=("Arial", 18), bg=headercolor).pack(pady=20)

        self.date_picker = DateEntry(content_frame, width=12, background='darkblue', foreground='white', borderwidth=2, state="readonly")
        self.date_picker.pack(pady=5)

        tk.Button(content_frame, text="Välj Datum", font=("Arial", 14), command=self.show_selected_date).pack(pady=10)

        self.datetext = tk.Label(content_frame, text="", font=("Arial", 16), bg=headercolor)
        self.datetext.pack(pady=20)

    def show_selected_date(self):
        selected_date = self.date_picker.get_date()
        total = get_total_on_date(self.collection, selected_date)
        self.datetext.config(text=f"Valt Datum: {selected_date} - Totalt: {total:.2f} kg")
