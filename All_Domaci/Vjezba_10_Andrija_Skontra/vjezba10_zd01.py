#Napišite program vjezba10_zd01.py koji crta kvadrat sa stranicom duljine 400 piksela, te
#njegove dijagonale. Također treba označiti vrhove kvadrata sa slovima A, B, C i D.

from turtle import *

speed(10)
pu()
goto(-200 , 200)
pd()
for i in 'ABCD':
    dot(10)
    pu()
    a, b = pos()
    goto(a + 10, b + 10)
    write(i)
    goto(a, b)
    pd()
    fd(400)
    rt(90)
rt(45)
fd(565.68542494924)

lt(135)
fd(400)
lt(135)
fd(565.68542494924)
hideturtle()

Screen().exitonclick()