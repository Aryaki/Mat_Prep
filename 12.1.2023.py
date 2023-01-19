import tkinter
file = open("C:/Users/skola/Desktop/subory/ciernobiely_obrazok_1.txt", "r")
line = file.readline()
width, height = line.split()
width = int(width)
height = int(height)
canvas = tkinter.Canvas(width=width, height=height, bg='white')
canvas.pack()
y = 0
for line in file:
    for x in range(width):
        shade = line[2 * x:2 * x + 2]
        color = "#" + 3 * shade

        canvas.create_rectangle(x, y, x+1, y+1, fill=color, width=0)
    canvas.update()
    y += 1
