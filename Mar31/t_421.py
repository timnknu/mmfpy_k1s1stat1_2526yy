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


class Car(Figure):
    def __init__(self, x0, y0):
        super().__init__(x0, y0)
        self._body = Rectangle( x0, y0, 200, 100)
        self._front_wheel = Circle(x0 + 200 - 50, y0 - 25, 50)
        self._back_wheel = Circle( x0 + 50 , y0 - 25, 50)
    def show(self):
        self._body.show()
        self._front_wheel.show()
        self._back_wheel.show()
    def hide(self):
        self._body.hide()
        self._front_wheel.hide()
        self._back_wheel.hide()


#
turtle.speed(3)

c = Car(-200, 100)
c.show()
c.hide()

turtle.mainloop()
# turtle.exitonclick()