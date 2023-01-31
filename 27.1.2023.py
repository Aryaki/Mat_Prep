import tkinter


canvas = tkinter.Canvas(width=400, height=1200, bg='white')
canvas.pack()

canvas.create_rectangle(100, 100, 300, 700, fill="black")

times = [500, 100, 500, 100]
colors = ["red", "orange", "green", "orange"]


def circle(x, y, col):
    canvas.create_oval(x-80, y-80, x+80, y+80, fill=col)


while True:
    x = 200
    y = 200

    for a in range(4):
        circle(x, y, colors[a])
        canvas.update()
        canvas.after(times[a])
        circle(x, y, "black")

        if a == 2:
            y -= 200

        else:
            y += 200



canvas.mainloop()









