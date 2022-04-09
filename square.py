import turtle

window = turtle.Screen()
cur = turtle.Pen()

cur.reset()
for i in range(1, 5):
    cur.forward(50)
    cur.left(90)

cur.reset()
for i in range(1, 9):
    cur.forward(100)
    cur.left(225)

cur.reset()
for i in range(1, 38):
    cur.forward(100)
    cur.left(175)

cur.reset()
for i in range(1, 20):
    cur.forward(100)
    cur.left(95)

cur.reset()
def star(star, fill):
    if fill == True:
        cur.begin_fill()
    for i in range(1, 19):
        cur.forward(star)
        if i % 2 == 0:
            cur.left(175)
        else:
            cur.left(225)
    if fill == True:
        cur.end_fill()
cur.color(0.9, 0.75, 0)        
star(120, True)
cur.color(0, 0, 0)
star(120, False)

window.exitonclick()