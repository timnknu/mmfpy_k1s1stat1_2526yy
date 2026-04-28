import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#tkinter.Toplevel
# https://docs.python.org/3/library/tkinter.html#tkinter.Toplevel.wm_overrideredirect
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.grab_set
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.wait_visibility
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.wait_window

def ask_name(parent):
    dialog = tk.Toplevel(parent)
    dialog.transient(parent)
    dialog.overrideredirect(True)

    value_var = tk.StringVar(value="Alice")
    result = {"value": None}

    frame = ttk.Frame(dialog, padding=10)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Modal dialog").pack(anchor="w")
    ttk.Label(frame, text="Name:").pack(anchor="w", pady=(8, 4))
    entry = ttk.Entry(frame, textvariable=value_var)
    entry.pack(fill="x")

    def accept(event=None):
        result["value"] = value_var.get()
        dialog.destroy()

    def cancel(event=None):
        dialog.destroy()

    ttk.Button(frame, text="OK", command=accept).pack(anchor="w", pady=(10, 4))
    ttk.Button(frame, text="Cancel", command=cancel).pack(anchor="w")

    dialog.bind("<Return>", accept)
    dialog.bind("<Escape>", cancel)

    dialog.update_idletasks()
    x = parent.winfo_rootx() + 40
    y = parent.winfo_rooty() + 40
    dialog.geometry(f"+{x}+{y}")

    dialog.wait_visibility()
    dialog.grab_set()
    entry.focus_set()
    parent.wait_window(dialog)
    return result["value"]


root = tk.Tk()
root.title("Custom modal dialog")

status = ttk.Label(root, text="Last result")
status.pack(fill="x", padx=10, pady=10)

def open_dialog():
    status.config(text=f"result = {ask_name(root)!r}")

ttk.Button(root, text="Open modal dialog", command=open_dialog).pack(anchor="w", padx=10)

root.mainloop()