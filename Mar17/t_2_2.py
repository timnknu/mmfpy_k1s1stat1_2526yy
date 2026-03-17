import turtle
import random
import math

turtle.speed(1)

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self._position = (0, 0)
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._color = "black"
        self._rot_angle = 0

    def set_rotation(self, alpha):
        self._rot_angle = alpha

    def set_position(self, x, y):
        self._position = (x, y)

    def set_color(self, color):
        self._color = color

    def _rotate_vec(self, x_old, y_old):
        x_rot = math.cos(self._rot_angle) * x_old + math.sin(self._rot_angle) * y_old
        y_rot = -math.sin(self._rot_angle) * x_old + math.cos(self._rot_angle) * y_old
        return x_rot, y_rot


    def draw(self):
        x0, y0 = self._position
        x1, y1 = self._rotate_vec(self._vertex1[0], self._vertex1[1])
        x2, y2 = self._rotate_vec(*self._vertex2)

        turtle.penup()
        turtle.goto(x0, y0)
        turtle.pendown()
        turtle.color(self._color)
        turtle.fillcolor(self._color)

        turtle.begin_fill()
        turtle.goto(x0+x1, y0+y1)
        turtle.goto(x0+x2, y0+y2)
        turtle.goto(x0, y0)
        turtle.end_fill()

tr = Triangle(100, 0, 0, 50)
tr.set_color('lime green')

for itr in range(10):
    tr.set_color('white')
    tr.draw()
    tr.set_color('lime green')
    tr.set_rotation(2*math.pi/10 * itr)
    tr.draw()


# for i in range(10):
#     R = [random.randint(-100, 100) for c in range(6)]
#
#     tr = Triangle(R[0], R[1], R[2], R[3])
#     tr.set_position(R[4], R[5])
#     tr.set_color('lime green')
#     tr.draw()


turtle.mainloop()
#turtle.exitonclick()