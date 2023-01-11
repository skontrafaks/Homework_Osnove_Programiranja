from turtle import *

speed(0)
n = 0
while (n < 2):
    n = int(textinput("N-terokut", "Unesi N"))

pu()
goto(-50, -50)
pd()
for i in range(n):
    dot(10)
    pu()
    a, b = pos()
    goto(a + 10, b + 10)
    write(str(i))
    goto(a, b)
    pd()
    fd(100)
    lt(360/n)

hideturtle()

Screen().exitonclick()
