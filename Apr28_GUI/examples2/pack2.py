import tkinter as tk

root = tk.Tk()

obj = tk.Label(root, text="TOP fill=X", bg="#8ecae6")
obj.pack(fill=tk.X)

tk.Label(root, text="LEFT\nfill=Y", bg="#ffb703").pack(side=tk.LEFT, fill=tk.Y)
tk.Label(root, text="RIGHT\nfill=Y", bg="#fb8500").pack(side=tk.RIGHT, fill=tk.Y)
tk.Text(root).pack(fill=tk.BOTH, expand=True)

def myfunc():
    root.destroy()

btn = tk.Button(root)
btn['text'] = 'Close'
btn['command'] = myfunc
btn.pack(side=tk.BOTTOM)

root.mainloop()



# from tkinter import *
#
# root = Tk()
#
# Label(root, text="TOP fill=X", bg="#8ecae6").pack(fill=X)
# Label(root, text="LEFT\nfill=Y", bg="#ffb703").pack(side=LEFT, fill=Y)
# Label(root, text="RIGHT\nfill=Y", bg="#fb8500").pack(side=RIGHT, fill=Y)
# Text(root).pack(fill=BOTH, expand=True)
# Button(root, text="Close", command=root.destroy).pack(side=BOTTOM)
#
# root.mainloop()


