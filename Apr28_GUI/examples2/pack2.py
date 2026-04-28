from tkinter import *

root = Tk()

Label(root, text="TOP fill=X", bg="#8ecae6").pack(fill=X)
Label(root, text="LEFT\nfill=Y", bg="#ffb703").pack(side=LEFT, fill=Y)
Label(root, text="RIGHT\nfill=Y", bg="#fb8500").pack(side=RIGHT, fill=Y)
Text(root).pack(fill=BOTH, expand=True)
Button(root, text="Close", command=root.destroy).pack(side=BOTTOM)

root.mainloop()
