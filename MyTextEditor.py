import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

# ----------- Setup Main Window -------------
window = tk.Tk()
window.title("Text Editor")
window.geometry("1200x600")
window.configure(bg="#2e2e2e")

# ----------- Theme Settings -------------
is_dark = True
light_theme = {"bg": "#ffffff", "fg": "#000000", "text_bg": "#ffffff", "text_fg": "#000000"}
dark_theme = {"bg": "#2e2e2e", "fg": "#ffffff", "text_bg": "#1e1e1e", "text_fg": "#ffffff"}

# ----------- Text Area -------------
txt_edit = tk.Text(window, wrap="word", undo=True, font=("Consolas", 14),
                   bg=dark_theme["text_bg"], fg=dark_theme["text_fg"], insertbackground="white")
txt_edit.pack(fill="both", expand=True, padx=2, pady=(2, 0))

# ----------- Status Bar -------------
status = tk.Label(window, text="Ready", anchor="w", bg="#444", fg="#fff", font=("Arial", 10))
status.pack(fill="x", side="bottom")

def update_status(event=None):
    content = txt_edit.get(1.0, tk.END)
    char_count = len(content.strip())
    status.config(text=f"Characters: {char_count}")

txt_edit.bind("<KeyRelease>", update_status)

# ----------- File Functions -------------
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            txt_edit.delete(1.0, tk.END)
            txt_edit.insert(tk.END, f.read())
            window.title(f"Text Editor - {filepath}")
            status.config(text="File loaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file:\n{e}")

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt",
                                  filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(txt_edit.get(1.0, tk.END))
            window.title(f"Text Editor - {filepath}")
            status.config(text="File saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")

# ----------- Edit Functions -------------
def cut(): txt_edit.event_generate("<<Cut>>")
def copy(): txt_edit.event_generate("<<Copy>>")
def paste(): txt_edit.event_generate("<<Paste>>")
def undo(): txt_edit.event_generate("<<Undo>>")
def redo(): txt_edit.event_generate("<<Redo>>")
def select_all(): txt_edit.tag_add("sel", "1.0", "end")

# ----------- Theme Toggle -------------
def toggle_theme():
    global is_dark
    theme = light_theme if is_dark else dark_theme
    txt_edit.config(bg=theme["text_bg"], fg=theme["text_fg"], insertbackground=theme["fg"])
    window.config(bg=theme["bg"])
    status.config(bg="#ccc" if not is_dark else "#444", fg=theme["fg"])
    is_dark = not is_dark
    status.config(text="Switched theme")

# ----------- Menu Bar -------------
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="📂 Open", command=open_file)
file_menu.add_command(label="💾 Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="❌ Exit", command=window.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Toggle Dark/Light Mode", command=toggle_theme)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Text Editor by Kanhaiya\nUsing Tkinter - Python"))

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="View", menu=view_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Initialize status
update_status()

# Start the main loop
window.mainloop()
