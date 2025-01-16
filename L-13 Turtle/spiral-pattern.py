import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
t=turtle.Turtle()
t.speed(20)
for i in range(1,100) :
    t.forward(i*3)
    t.right(90)
turtle.hideturtle()
turtle.done()
