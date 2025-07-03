import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
t=turtle.Turtle()
sl=70
ts=6
ang=360/ts
for i in range(0,ts) :
    t.forward(sl)
    t.right(ang)
turtle.done()