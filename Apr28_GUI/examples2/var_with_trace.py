# https://www.geeksforgeeks.org/python/tracing-tkinter-variables-in-python/

from tkinter import *

root = Tk()
var = StringVar()

def on_button():
    current = var.get()          # read
    print("User typed:", current)
    var.set(current.upper())     # write (updates UI immediately)

def on_change(*args):
    print("Changed to:", var.get())

var.trace_add("write", on_change)

Entry(root, textvariable=var).pack()
Label(root, textvariable=var).pack()
Button(root, text="Process", command=on_button).pack()

root.mainloop()
