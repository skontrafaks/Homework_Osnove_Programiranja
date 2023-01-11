from turtle import *
import math

t1 = Turtle()
t2 = Turtle()
t1.speed(0)
t2.speed(0)

n = 0
while (n < 2):
    n = int(textinput("N-terokut", "Unesi N"))

r = 200
d = 2*r*math.sin(math.pi/n)
t1.pu()
t1.goto(-d/2, -d/2)
t1.pd()
for i in range(n):
    t1.fd(d)
    t1.lt(360/n)
x, y = t1.pos()
t2.pu()
t2.goto(x, y)
t2.pd()
t2.fillcolor("red")
t2.begin_fill()
t2.rt((360/n)/2)
t2.circle(r)
t2.end_fill()
t1.fillcolor("blue")
t1.begin_fill()
for i in range(n):
    t1.fd(d)
    t1.lt(360/n)
t1.end_fill()
t1.hideturtle()
t2.hideturtle()

Screen().exitonclick()