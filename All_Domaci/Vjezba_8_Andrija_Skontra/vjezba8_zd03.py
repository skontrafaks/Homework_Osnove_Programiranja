x = int(input("unesi X koordinatu točke T\n"))
y = int(input("unesi Y koordinatu točke T\n"))

def kvadrant(x,y):
    if x > 0 and y > 0:
        return "u prvom kvadrantu"
    if x < 0 and y > 0:
        return "u drugom kvadrantu"
    if x < 0 and y < 0:
        return "u trećem kvadrantu"
    if x > 0 and y < 0:
        return "u četvrtom kvadrantu"
    if x == 0 and y != 0:
        return "na X osi"
    elif y == 0 and x != 0:
        return "na Y osi"
    else:
        return "u ishodistu"

print(f'Točka T se nalazi {kvadrant(x,y)}')