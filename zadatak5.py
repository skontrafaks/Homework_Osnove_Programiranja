from turtle import *

speed(0)
n = int(textinput("Kruznica", "Unesi n"))
n = n/2
pu()
goto(0, -n)
pd()
pencolor("#737373")
circle(n)
fillcolor("#737373")
begin_fill()
circle(n, 360, 5)
end_fill()
ht()

mainloop()