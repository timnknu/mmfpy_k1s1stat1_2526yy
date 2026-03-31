import turtle

class Figure:
    def __init__(self, x0, y0):
        self._x0 = x0
        self._y0 = y0
        self._color = 'red'
        self._is_visible = False
    def set_color(self, color):
        self._color = color
    def _draw(self):
        raise NotImplementedError("Зробіть спершу дочірній клас")
    def show(self):
        if not self._is_visible:
            turtle.color(self._color)
            self._draw()
        self._is_visible = True
    def hide(self):
        if self._is_visible:
            turtle.color('white')
            self._draw()
        self._is_visible = False

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

class Rectangle(Figure):
    def __init__(self, x0, y0, sideX, sideY):
        self._a = sideX
        self._b = sideY
        super().__init__(x0, y0)
    def set_dimens(self, a, b):
        self._a = a
        self._b = b
    def _draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0)
        turtle.pendown()
        turtle.goto(self._x0, self._y0 + self._b)
        turtle.goto(self._x0 + self._a, self._y0 + self._b)
        turtle.goto(self._x0 + self._a, self._y0)
        turtle.goto(self._x0, self._y0)

class Square(Rectangle):
    def __init__(self, x0, y0, a):
        super().__init__(x0, y0, a, a)
    def set_dimens(self, a, b):
        raise NotImplementedError
        #assert a==b
        #super().set_dimens(a, b)


#
turtle.speed(1)

#s = Rectangle(100, 100, 80, 120)
s = Square(100, 100, 80)
s.set_color('red')
#s.set_dimens(100, 200)
s.show()
s.show()
s.hide()


# c = Circle(100, 100, 50)
# c.draw()
# c.hide()

turtle.mainloop()
# turtle.exitonclick()