from tkcalendar import DateEntry
import tkinter as tk

class Page3(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor):
        super().__init__(parent, bg=backgroundcolor)

        content_frame = tk.Frame(self, bg=headercolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(content_frame, text="Specific Day", font=("Arial", 18), bg=headercolor).pack(pady=20)

        self.date_picker = DateEntry(content_frame, width=12, background='darkblue', foreground='white', borderwidth=2,state="readonly")
        self.date_picker.pack(pady=5)

        tk.Button(content_frame, text="Confirm Date", font=("Arial", 14), command=self.show_selected_date).pack(pady=10)

        # Assign the label to an instance variable
        self.datetext = tk.Label(content_frame, text="", font=("Arial", 16), bg=headercolor)
        self.datetext.pack(pady=20)

    def show_selected_date(self):
        selected_date = self.date_picker.get_date()
        # Update the label text using the instance variable
        self.datetext.config(text=f"Selected date: {selected_date}")
        print("Selected date:", selected_date)
