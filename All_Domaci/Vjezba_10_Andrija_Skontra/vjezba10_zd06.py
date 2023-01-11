from turtle import *

speed(0)
colormode(255)
r = 300
a, b, c = 255, 255, 255
pu()
goto(0, -300)
pd()
for i in range(10):
    color(int(a), int(b), int(c))
    begin_fill()
    circle(r)
    end_fill()
    old_r = r
    r *= 0.9
    a *= 0.95
    b *= 0.95
    c *= 0.95
    x, y = pos()
    pu()
    goto(x, y + (old_r - r))
    pd()
hideturtle()
Screen().exitonclick()