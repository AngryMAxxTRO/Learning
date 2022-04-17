from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(0, 60):
    canvas.move(1, 5, 5)
    tk.update()
    time.sleep(0.05)


def move_triangle(event):
    canvas.move(1, 5, 0)


canvas.bind_all('<KeyPress-Return', move_triangle())
