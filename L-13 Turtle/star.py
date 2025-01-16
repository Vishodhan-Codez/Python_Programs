import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
t=turtle.Turtle()
for i in range(0,3) :
    t.forward(100)
    t.left(120)
t.right(270)
t.penup()
t.forward(50)
t.right(90)
t.pendown()
for i in range(0,3) :
    t.forward(100)
    t.right(120)
turtle.hideturtle()
turtle.done()
