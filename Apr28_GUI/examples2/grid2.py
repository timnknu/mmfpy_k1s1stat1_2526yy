from tkinter import *

root = Tk()
root.columnconfigure(1, weight=1)

Label(root, text="Header", bg="#b0c4de").grid(row=0, column=0, columnspan=3, sticky="ew")
Label(root, text="Name:").grid(row=1, column=0)
Entry(root).grid(row=1, column=1, sticky="ew")
Button(root, text="Go").grid(row=1, column=2)
Text(root, height=4).grid(row=2, column=0, columnspan=3, sticky="ew")
Button(root, text="OK").grid(row=3, column=2)

root.mainloop()
