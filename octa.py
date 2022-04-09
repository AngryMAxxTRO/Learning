import turtle

window = turtle.Screen()

cur = turtle.Pen()
def octa(side, fill):
    if fill == True:
        cur.begin_fill()
    for i in range(1, 9):
        cur.forward(side)
        cur.left(45)
    if fill == True:
        cur.end_fill()    

cur.color(0.9, 0.75, 0)        
octa(50, True)
cur.color(0, 0, 0)
octa(50, False)

cur.reset()
a = 100
b = 10
def star(star, fill, ray):
    angle = 360 / ray
    if fill == True:
        cur.begin_fill()
    for i in range(0, ray):
        cur.forward(star)
        cur.left(180 - angle)
        cur.forward(star)
        cur.right(180 - (angle * 2))
    if fill == True:
        cur.end_fill()

cur.color(0.9, 0.75, 0)        
star(a, True, b)
cur.color(0, 0, 0)
star(a, False, b)

window.exitonclick()