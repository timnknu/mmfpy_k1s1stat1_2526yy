from tkinter import *

root = Tk()

var = StringVar()
Entry(root, textvariable=var).pack()
Label(root, textvariable=var).pack()

root.mainloop()
