import tkinter
import random as rn

canvas = tkinter.Canvas(width=200, height=200, bg='white')
canvas.pack()


x = 20

for i in range(8):
    if i == 0 or i == 7:
        line = rn.randint(1, 9)

    else:
        line = rn.randint(0, 9)

    if line != 0:
        canvas.create_line(x+i*10,10, x+i*10,90, width=line)

    canvas.create_text(x+i*10, 110, text=line)

canvas.mainloop()
