from turtle import *
import math

speed(0)
n = 0
while (n < 2):
    n = int(textinput("N-terokut", "Unesi N"))

r = 200
d = 2*r*math.sin(math.pi/n)
pu()
goto(-d/2, -d/2)
pd()
for i in range(n):
    fd(d)
    lt(360/n)
rt((360/n)/2)
circle(r)

Screen().exitonclick()