from turtle import *

speed(0)
ht()

radijus = 300
colormode(255)
boja = 255

for i in range(10):
    pu()
    goto(0, -radijus)
    pd()

    fillcolor(int(boja), int(boja), int(boja))

    begin_fill()
    circle(radijus)
    end_fill()

    boja *= 0.95
    
    radijus *= 0.9
    
Screen().exitonclick()
