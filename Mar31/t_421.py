import turtle

class Figure:
    def __init__(self, x0, y0):
        self._x0 = x0
        self._y0 = y0
        self._color = 'red'
    def set_color(self, color):
        self._color = color

class Circle(Figure):
    def __init__(self, x0, y0, radius):
        self._r = radius
        super().__init__(x0, y0)
    def set_radius(self, r):
        self._r = r
    def draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0 - self._r)
        turtle.pendown()
        turtle.circle(self._r)
    def hide(self):
        turtle.color('white')
        self.draw()

class Square(Figure):
    def __init__(self, x0, y0, side):
        self._a = side
        super().__init__(x0, y0)
    def set_side(self, a):
        self._a = a
    def draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0)
        turtle.pendown()
        turtle.goto(self._x0, self._y0 + self._a)
        turtle.goto(self._x0 + self._a, self._y0 + self._a)
        turtle.goto(self._x0 + self._a, self._y0)
        turtle.goto(self._x0, self._y0)
    def hide(self):
        turtle.color('white')
        self.draw()



#
turtle.speed(1)

s = Square(100, 100, 80)
s.draw()
s.hide()

# c = Circle(100, 100, 50)
# c.draw()
# c.hide()

turtle.mainloop()
# turtle.exitonclick()