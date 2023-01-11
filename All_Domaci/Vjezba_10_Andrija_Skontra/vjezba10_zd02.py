from turtle import *

duljina = float(textinput("DULJINA", "Unesi"))

def kvadrat(duljina):
    pu()
    goto(-duljina / 2, duljina / 2)
    pd()
    for i in range(4):
        fd(duljina)
        rt(90)

kvadrat(duljina)