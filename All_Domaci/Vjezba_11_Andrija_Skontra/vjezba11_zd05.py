from turtle import *
from random import randrange
#n = int(textinput("Unesi bron izmedu 0 i 50"))
colormode(255)
boja = 150
speed(0)
n = 30
p = 300
for i in range(5):
    fillcolor(int(boja), int(boja), int(boja))
    begin_fill()
    fd(p)
    lt(120)
    fd(p)
    lt(120)
    fd(p)
    lt(120)
    home()
    end_fill()
    p -= n
    boja = randrange(50,200)

Screen().exitonclick()
