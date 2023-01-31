from turtle import *
from random import  choice
import time
speed(0)
n, stranica_tr = 100, 100
boje=["red","gray","blue","purple","yellow", "black"]
for i in range(6):
    nasa_boja = choice(boje)
    pencolor(nasa_boja)
    boje.remove(nasa_boja)
    for j in range(4):
        fd(n)
        lt(360/4)
    n = n*1.11
lt(60)
fillcolor("green")
begin_fill()
for i in range(3):
    fd(stranica_tr)
    lt(120)
end_fill()

mainloop()