# time period

import tkinter as tk

class Page2(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor):
        super().__init__(parent, bg=backgroundcolor)

        content_frame = tk.Frame(self, bg=headercolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        tk.Label(content_frame, text="Timeframe", font=("Arial", 18), bg=headercolor).pack(pady=50)
