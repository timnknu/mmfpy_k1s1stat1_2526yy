import turtle

class Figure:
    def __init__(self, x0, y0):
        self._x0 = x0
        self._y0 = y0
        self._color = 'red'
    def set_color(self, color):
        self._color = color
    def _draw(self):
        raise NotImplementedError("Зробіть спершу дочірній клас")
    def show(self):
        turtle.color(self._color)
        self._draw()
    def hide(self):
        turtle.color('white')
        self._draw()

f = Figure(10, 10)
f.show()


class Circle(Figure):
    def __init__(self, x0, y0, radius):
        self._r = radius
        super().__init__(x0, y0)
    def set_radius(self, r):
        self._r = r
    def _draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0 - self._r)
        turtle.pendown()
        turtle.circle(self._r)

class Square(Figure):
    def __init__(self, x0, y0, side):
        self._a = side
        super().__init__(x0, y0)
    def set_side(self, a):
        self._a = a
    def _draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0)
        turtle.pendown()
        turtle.goto(self._x0, self._y0 + self._a)
        turtle.goto(self._x0 + self._a, self._y0 + self._a)
        turtle.goto(self._x0 + self._a, self._y0)
        turtle.goto(self._x0, self._y0)



#
turtle.speed(1)

s = Square(100, 100, 80)
s._draw()
s.hide()

# c = Circle(100, 100, 50)
# c.draw()
# c.hide()

turtle.mainloop()
# turtle.exitonclick()