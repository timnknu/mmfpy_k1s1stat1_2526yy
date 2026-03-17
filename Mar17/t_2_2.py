import turtle

turtle.speed(1)

x0, y0 = -100, -80
x1, y1 = 120, 150
x2, y2 = -120, 190


turtle.penup()
turtle.goto(x0, y0)
turtle.pendown()

turtle.goto(x0+x1, y0+y1)
turtle.goto(x0+x2, y0+y2)
turtle.goto(x0, y0)

turtle.mainloop()
#turtle.exitonclick()