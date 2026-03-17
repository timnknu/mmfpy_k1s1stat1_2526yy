import turtle

turtle.speed(1)

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self._position = (0, 0)
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        #self._color = "black"

    def set_position(self, x, y):
        self._position = (x, y)
    def set_color(self, color):
        self._color = color

    def draw(self):
        x0, y0 = self._position
        x1, y1 = self._vertex1
        x2, y2 = self._vertex2

        turtle.penup()
        turtle.goto(x0, y0)
        turtle.pendown()

        turtle.goto(x0+x1, y0+y1)
        turtle.goto(x0+x2, y0+y2)
        turtle.goto(x0, y0)

tr = Triangle(120, 50, 30, 180)
tr.set_position(50, 60)
tr.draw()

another_tr = Triangle(-120, -150, -30, -80)
another_tr.draw()


turtle.mainloop()
#turtle.exitonclick()