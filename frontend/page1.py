# Dashboard

import tkinter as tk

class Page1(tk.Frame):
    def __init__(self, parent, headercolor, backgroundcolor):
        super().__init__(parent, bg=backgroundcolor)
        
        content_frame = tk.Frame(self, bg=backgroundcolor)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        content_frame.rowconfigure(0, weight=1)

        left_box = tk.Frame(content_frame, bg=headercolor, relief="ridge", borderwidth=2)
        left_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(left_box, text="Info", bg=headercolor, font=("Arial", 16)).pack(expand=True)

        right_box = tk.Frame(content_frame, bg=headercolor, relief="ridge", borderwidth=2)
        right_box.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(right_box, text="Info", bg=headercolor, font=("Arial", 16)).pack(expand=True)
