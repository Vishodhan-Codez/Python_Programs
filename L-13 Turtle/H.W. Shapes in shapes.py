import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(400, 400)
t = turtle.Turtle()
t.color("white")
t.speed(30)
s = 200
t.penup()
t.goto(-s/2, -s/2)
t.pendown()
for i in range(0,4):
    t.forward(s)
    t.left(90)
t.penup()
h = (3**0.5/2) *s
t.goto(-h/2,-h/(3**0.5))
t.pendown()
for j in range(3):
    t.forward(h)
    t.left(120)
t.penup()
t.goto(0, -h/(3**0.5))
t.pendown()
t.circle(h/(3**0.5))
t.hideturtle()
turtle.done()
