import tkinter

canvas = tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

x = 400
y = 300
dx = 5
dy = 5

while True:
    canvas.create_oval(x-25, y-25, x+25, y+25, width=1, tags="ball", fill="black")

    if y >= 575 or y <= 25:
        dy = -dy

    if x >= 775 or x <= 25:
        dx = -dx

    x=x+dx
    y=y+dy
    canvas.after(20)
    canvas.update()
    canvas.delete("ball")

canvas.mainloop()












