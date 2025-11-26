from tkcalendar import DateEntry
import tkinter as tk
from backend import get_total_on_date
from datetime import date

# specific day

class Page3(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor, collection):
        super().__init__(parent, bg=backgroundcolor)
        self.collection = collection

        content_frame = tk.Frame(self, bg=headercolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(content_frame, text="Specifik Dag", font=("Arial", 18), bg=headercolor).pack(pady=20)
        self.date_picker = DateEntry(content_frame, width=12, background='darkblue', foreground='white', borderwidth=2, state="readonly")
        self.date_picker.pack(pady=5)

        tk.Button(content_frame, text="Välj Datum", command=self.show_selected_date).pack(pady=10)
        self.datetext = tk.Label(content_frame, text="", font=("Arial", 16), bg=headercolor)
        self.datetext.pack(pady=20)

    def show_selected_date(self, selected_date=None):
        if selected_date is None:
            selected_date = self.date_picker.get_date()
        total_waste, total_students = get_total_on_date(self.collection, selected_date)
        avg = total_waste / total_students if total_students else 0
        self.datetext.config(
            text=f"{selected_date}:\nMatavfall: {total_waste:.2f} kg\n"
                 f"Elever åt: {total_students}\n"
                 f"Genomsnitt per elev: {avg:.2f} kg"
        )

    def update_stats(self):
        # Show today by default when switching to the page
        self.show_selected_date(date.today())
