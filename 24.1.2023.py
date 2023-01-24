import tkinter

x, y = 250, 250
canvas = tkinter.Canvas(width=500, height=500, bg='white')
canvas.pack()


def key(e):
    global sx, sy

    if e.keysym == "Left":
        sx, sy = -1, 0

    elif e.keysym == "Right":
        sx, sy = 1, 0

    elif e.keysym == "Up":
        sx, sy = 0, -1

    elif e.keysym == "Down":
        sx, sy = 0, 1

sx, sy = 0, -1

end = True

while end:
    if x < 0 or x > 500 or y < 0 or y > 500:
        end = False

    else:
        canvas.create_line(x, y, x+sx, y+sy, fill="black", width=5)
        x += sx
        y += sy
        canvas.after(5)
        canvas.update()
    canvas.bind_all("<Key>", key)


canvas.mainloop()
























