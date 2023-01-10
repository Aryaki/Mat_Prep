file = open("C:/Users/skola/Desktop/subory/skok_do_dialky.txt", "r")
lines = file.readlines()

wins = []

for i in range(len(lines)):
    maximum = 0
    for j in range(len(lines[0].split(" ")) -1):
        if int(lines[i].strip("\n").split(" ")[1:][j]) > maximum:
            maximum = int(lines[i].strip("\n").split(" ")[1:][j])

    wins.append(maximum)

max(wins)

################################################################
import tkinter
file = open("C:/Users/skola/Desktop/subory/komprimovany_obrazok_1.txt", "r")
line = file.readline()
width, height = line.split()
width = int(width)
height = int(height)
canvas = tkinter.Canvas(width=width, height=height, bg='white')
canvas.pack()
y = 0
for line in file:
    line = line.split(" ")
    x = 0
    color = True
    for num in line:
        num = int(num)
        if color:
            canvas.create_rectangle(x, y, x + num, y + 1, fill="black")
        x += num
        color = not color
    y += 1




















