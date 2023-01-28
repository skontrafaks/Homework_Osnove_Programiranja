from turtle import *

n = int(input("Unesi prirodan broj izmedu 0-300: "))
speed(0) #maks brzina crtanja

#moramo se staviti u poziciju da nam je centar kruga u sredini
pu()
goto(0, -n/2)
pd()
#crtamo krug
circle(n)

#crtamo peterokut
color('black')
begin_fill()
circle(n, 360, 5)
end_fill()

#sakrijemo kornjacu i zavrsimo
ht()
mainloop()