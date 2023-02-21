import tkinter

canvas = tkinter.Canvas(width=800, height=800, bg='white')
canvas.pack()

x = 400
y = 400
dx = 3
dy = 2

while True:

    canvas.create_oval(x, y, x+40, y+40, tags="ball", fill="black")

    x += dx
    y += dy

    if x > 760 or x < 40:
        dx = -dx

    elif y > 775 or y < 25:
        dy = -dy

    canvas.after(15)
    canvas.update()
    canvas.delete("ball")

canvas.mainloop()
