import tkinter as tk
from page1 import Page1
from page2 import Page2
from page3 import Page3

def show_frame(frame):
    frame.tkraise()
    update_header_buttons(frame)

def update_header_buttons(active_frame):
    for page, button in header_buttons.items():
        if page == active_frame:
            button.config(text=f"{page_titles[page]} (current)", state="disabled")
        else:
            button.config(text=page_titles[page], state="normal")

window = tk.Tk()
window.title("Matsvinn NTI")
window.geometry("1024x640")
window.configure(bg="#EDEDED")

headercolor="#FFFFFF"
backgroundcolor="#333333"

container = tk.Frame(window, bg=backgroundcolor)
container.pack(fill="both", expand=True)
container.rowconfigure(0, weight=1)
container.columnconfigure(0, weight=1)

# Create pages
page1 = Page1(container, headercolor, backgroundcolor)
page2 = Page2(container, headercolor, backgroundcolor)
page3 = Page3(container, headercolor, backgroundcolor)

for page in (page1, page2, page3):
    page.grid(row=0, column=0, sticky="nsew")

page_titles = {
    page1: "Dashboard",
    page2: "Timeframe",
    page3: "Specific Day"
}

header_buttons = {}

# Shared header
header_frame = tk.Frame(window, bg=headercolor, height=60)
header_frame.pack(fill="x")
header_frame.pack_propagate(False)
tk.Label(header_frame, text="Matsvinn NTI", bg=headercolor, font=("Arial", 20, "bold")).pack(side="left", padx=10)

btn_dash = tk.Button(header_frame, font=("Arial", 14), command=lambda: show_frame(page1))
btn_time = tk.Button(header_frame, font=("Arial", 14), command=lambda: show_frame(page2))
btn_day  = tk.Button(header_frame, font=("Arial", 14), command=lambda: show_frame(page3))

btn_dash.pack(side="right", padx=5)
btn_time.pack(side="right", padx=5)
btn_day.pack(side="right", padx=5)

header_buttons[page1] = btn_dash
header_buttons[page2] = btn_time
header_buttons[page3] = btn_day

# Show Page 1 initially
show_frame(page1)

window.mainloop()
