from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create main window
root = Tk()
root.title("Digital Clock")
root.geometry("650x200")
root.resizable(False, False)
root.configure(bg="#101820")

# Clock font settings
clock_font = ("ds-digital", 72)

# Time Label
time_label = Label(
    root,
    font=clock_font,
    background="#101820",
    foreground="#00FFFF",
    anchor="center"
)
time_label.pack(expand=True)

# Date Label
date_label = Label(
    root,
    font=("Helvetica", 18, "bold"),
    background="#101820",
    foreground="#FFFFFF"
)
date_label.pack()

# Update time every second
def update_time():
    current_time = strftime("%H:%M:%S %p")
    current_date = strftime("%A, %d %B %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

update_time()
root.mainloop()
