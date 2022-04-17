import turtle

window = turtle.Screen()

t = turtle.Pen()

t.color(1, 0, 0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
t.color(0, 0, 0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

t.up()
t.backward(200)
t.down()


def circle(r, g, b):
    t.color(r, g, b)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


circle(0, 1, 0)
circle(1, 0.5, 0)
circle(1, 0, 0)
circle(0.5, 0, 0)
circle(0, 0, 1)
circle(0, 0, 0.5)
circle(0.9, 0.75, 0)
circle(1, 0.7, 0.75)
circle(1, 0.5, 0)
circle(0.9, 0.5, 0.15)
circle(0, 0, 0)
circle(1, 1, 1)

t.reset()


def square(side):
    if fill:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(side)
        t.left(90)
    if fill:
        t.end_fill()
    for x in range(1, 5):
        t.forward(side)
        t.left(-90)
    for x in range(1, 5):
        t.back(side)
        t.right(90)
    if fill:
        t.begin_fill()
    for x in range(1, 5):
        t.back(side)
        t.right(-90)
    if fill:
        t.end_fill()


fill = False
square(25)
fill = True
square(50)
fill = False
square(75)
fill = True
square(100)
fill = False
square(125)
fill = True
square(150)
fill = False
square(175)
fill = True
square(200)

window.exitonclick()
