import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html
# https://docs.python.org/3/library/tkinter.ttk.html#entry
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Entry + StringVar")

value_var = tk.StringVar(value="Initial text")

entry = ttk.Entry(root, textvariable=value_var)
entry.pack(fill="x", padx=10, pady=10)

status = ttk.Label(root)
status.pack(fill="x", padx=10, pady=(0, 10))

def read_value():
    print('The value is', value_var.get())
    status.config(text=f"entry.get() = {entry.get()!r}; StringVar.get() = {value_var.get()!r}")

def set_with_variable():
    value_var.set("set via StringVar")
    read_value()

def set_with_widget():
    entry.delete(0, tk.END)
    entry.insert(0, "set via Entry")
    read_value()

ttk.Button(root, text="Read", command=read_value).pack(anchor="w", padx=10)
ttk.Button(root, text="Set via StringVar", command=set_with_variable).pack(anchor="w", padx=10, pady=4)
ttk.Button(root, text="Set via Entry", command=set_with_widget).pack(anchor="w", padx=10)

root.mainloop()