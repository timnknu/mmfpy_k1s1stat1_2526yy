import tkinter as tk


# Docs:
# https://docs.python.org/3/library/tkinter.html#the-canvas-widget
# https://docs.python.org/3/library/tkinter.html#images

def build_image():
    image = tk.PhotoImage(width=80, height=80)
    for x in range(80):
        for y in range(80):
            color = "#3a7" if (x // 10 + y // 10) % 2 == 0 else "#f7d774"
            image.put(color, (x, y))
    return image


root = tk.Tk()
root.title("Canvas drawing + image")

canvas = tk.Canvas(root, width=420, height=280, bg="white")
canvas.pack(padx=10, pady=10)

canvas.create_line(20, 20, 200, 20, width=3, fill="navy")
canvas.create_rectangle(20, 50, 140, 130, outline="darkgreen", width=2)
canvas.create_oval(170, 50, 290, 130, fill="tomato", outline="")
canvas.create_text(80, 160, text="Canvas text")

image = build_image()
canvas.image = image
canvas.create_image(340, 90, image=image)

root.mainloop()