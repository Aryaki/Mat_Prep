import tkinter

canvas = tkinter.Canvas(width=500, height=500, bg='white')
canvas.pack()

for i in range(0, 500, 50):
    canvas.create_line(i, 0, i, 500)
    canvas.create_line(0, i, 500, i)

turn = True


def game(pos):
    global turn

    x = (pos.x // 50) * 50 + 25
    y = (pos.y // 50) * 50 + 25

    if turn:
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, width=5)

    else:
        canvas.create_line(x - 20, y - 20, x + 20, y + 20, width=5)
        canvas.create_line(x + 20, y - 20, x - 20, y + 20, width=5)

    turn = not turn


canvas.bind('<Button-1>', game)

canvas.mainloop()
