from tkinter import *
from tkinter import colorchooser
import random
import turtle

window = turtle.Screen()


def hello():
    print("Hello!")


a = 100
s_width = 400
s_height = s_width
r_width = 350
r_height = r_width


def rand_choice():
    choose = ["cyan", "green", "red", "blue", "orange", "yellow", "pink", "purple", "violet", "magenta"]
    random.shuffle(choose)
    randcolor = random.choice(choose)
    return r_width, r_height, randcolor


def rand_hex():
    palette = 255 * 255 * 255
    rand_list = []
    randcolor = ("#%06x" % random.randrange(palette))
    if randcolor in rand_list:
        randcolor.replace(randcolor, ("#%06x" % random.randrange(palette)))
    else:
        rand_list.append(randcolor)
    return r_width, r_height, str(rand_list[-1])


def ask_color():
    randcolor = str(colorchooser.askcolor()[1])
    return r_width, r_height, randcolor


tk = Toplevel()
btn = Button(tk, text="Click ME!", command=hello)
btn.pack()
canvas = Canvas(tk, width=s_width, height=s_height)
canvas.pack()


def rand_rect(width, height, color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    return canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)


def rand_oval(width, height, color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    return canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def rand_tria(width, height, color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    x3 = x2 + random.randrange(width)
    y3 = x2 + random.randrange(height)
    return canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color, outline=color)


def rand_quad(width, height, color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    x3 = x2 + random.randrange(width)
    y3 = x2 + random.randrange(height)
    x4 = x3 + random.randrange(width)
    y4 = y3 + random.randrange(height)
    return canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=color, outline=color)


for i in range(0, a):
    rand_rect(
        rand_choice()[0],
        rand_choice()[1],
        rand_choice()[2],
    )
    rand_oval(
        rand_hex()[0],
        rand_hex()[1],
        rand_hex()[2],
    )
    rand_tria(
        rand_choice()[0],
        rand_choice()[1],
        rand_choice()[2],
    )
    rand_quad(
        rand_hex()[0],
        rand_hex()[1],
        rand_hex()[2],
    )

canvas.create_text(150, 150, text="Times", font=("Times", 15))
canvas.create_text(200, 200, text="Helvetica", font=("Helvetica", 20))
canvas.create_text(220, 250, text="Courier", font=("Courier", 22))
canvas.create_text(220, 300, text="Arial", font=("Arial", 26))

image = PhotoImage(file="img.gif")
canvas.create_image(0, 0, anchor=NW, image=image)

window.exitonclick()
