import tkinter as tk

root = tk.Tk()

for i in range(10):
    btn = tk.Button(root)
    btn['text'] = 'Close'
    btn.pack(side=tk.BOTTOM, pady=20)


root.mainloop()


