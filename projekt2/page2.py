from backend import get_total_in_period
import tkinter as tk

# timeline

class Page2(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor, collection):
        super().__init__(parent, bg=backgroundcolor)
        self.collection = collection

        content_frame = tk.Frame(self, bg=headercolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(content_frame, text="Tidsperiod", font=("Arial", 18), bg=headercolor).pack(pady=20)
        button_frame = tk.Frame(content_frame, bg=headercolor)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Senaste Veckan", command=lambda: self.show_period(7)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Senaste Månaden", command=lambda: self.show_period(30)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Senaste Året", command=lambda: self.show_period(365)).pack(side="left", padx=10)

        self.result_label = tk.Label(content_frame, text="", font=("Arial", 16), bg=headercolor)
        self.result_label.pack(pady=20)

    def show_period(self, days):
        total_waste, total_students = get_total_in_period(self.collection, days)
        avg = total_waste / total_students if total_students else 0
        self.result_label.config(
            text=f"Totalt matavfall senaste {days} dagar: {total_waste:.2f} kg\n"
                 f"Totala elever åt: {total_students}\n"
                 f"Genomsnittligt matavfall per elev: {avg:.2f} kg"
        )

    def update_stats(self):
        # Default display last 7 days
        self.show_period(7)
