from turtle import *
from random import randint

colormode(255)
broj_tocaka = textinput("Broj tocaka", "Upisi broj tocaka:")
velicina_tocke = textinput("Velicina", "Unesi velicinu tocke:")

def color():
    r = randint(0,255)
    t = randint(0,255)
    z = randint(0,255)
    return (r, t, z)

for i in range(int(broj_tocaka)):
    pu()
    goto(randint(-300, 300), randint(-300, 300))
    dot(velicina_tocke, color())
    x, y = pos()
    goto(x + int(velicina_tocke)//2, y + int(velicina_tocke)//2)
    write(f"{int(x)}, {int(y)}")
    goto(x, y)

hideturtle()
Screen().exitonclick()


