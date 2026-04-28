import tkinter as tk
from tkinter import messagebox, ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#menus-and-toolbars
# https://docs.python.org/3/library/tkinter.html#tkinter.Menu

root = tk.Tk()
root.title("Menus")

show_status_var = tk.BooleanVar(value=True)
theme_var = tk.StringVar(value="Light")
status_var = tk.StringVar()

content = ttk.Frame(root, padding=10)
content.pack(fill="both", expand=True)
status_label = ttk.Label(content, textvariable=status_var)
status_label.pack(anchor="w")

def refresh_status():
    if show_status_var.get():
        status_label.pack(anchor="w")
    else:
        status_label.pack_forget()
    status_var.set(f"theme={theme_var.get()}, show_status={show_status_var.get()}")

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Refresh", command=refresh_status)
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

view_menu = tk.Menu(menubar, tearoff=False)
view_menu.add_checkbutton(label="Show status", variable=show_status_var, command=refresh_status)
view_menu.add_radiobutton(label="Light", variable=theme_var, value="Light", command=refresh_status)
view_menu.add_radiobutton(label="Dark", variable=theme_var, value="Dark", command=refresh_status)
menubar.add_cascade(label="View", menu=view_menu)

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Menu example", parent=root))
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)
refresh_status()
root.mainloop()