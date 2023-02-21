import tkinter
import math

canvas = tkinter.Canvas(width=1000, height=1000, bg='white')
canvas.pack()

canvas.create_oval(300, 200, 700, 600, width=6, outline="red")
u = 0

for i in range(12):
    x = int(200 * math.cos(u)) + 500
    y = int(200 * math.sin(u)) + 400
    u += math.pi / 6
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")

u = -2*math.pi / 6
for i in range(12):
    x = 180 * math.cos(u) + 500
    y = 180 * math.sin(u) + 400
    u += math.pi / 6
    canvas.create_text(x, y, text=i+1, font=("Arial", "12"))

u = -math.pi / 2
for i in range(60):
    x = 150 * math.cos(u) + 500
    y = 150 * math.sin(u) + 400
    u += math.pi / 30
    canvas.create_line(500, 400, x, y, fill="black", tags="hand", width=6)
    canvas.after(1000)
    canvas.update()
    canvas.delete("hand")



canvas.mainloop()

