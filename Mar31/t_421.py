import turtle

class Figure:
    def __init__(self, x0, y0):
        self._x0 = x0
        self._y0 = y0
        self._color = 'red'
    def set_color(self, color):
        self._color = color

class Circle(Figure):
    def __init__(self, x0, y0):
        self._r = None
        super().__init__(x0, y0)
    def set_radius(self, r):
        self._r = r
    def draw(self):
        if self._r is None:
            raise ValueError("Встановіть радіус")
        turtle.penup()
        turtle.goto(self._x0, self._y0 - self._r)
        turtle.pendown()
        turtle.circle(self._r)


#
turtle.speed(1)

c = Circle(100, 100)
c.draw()

turtle.mainloop()
# turtle.exitonclick()