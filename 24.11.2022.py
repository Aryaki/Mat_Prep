f = open("PINs.txt", "w")

for i in range(6):
    for j in range(0, 10, 2):
        for k in range(6):
            for l in range(1, 10, 2):
                print(f"{i}{j}{k}{l}", file=f)


f.close()

################################################################

file = open("C:/Users/skola/Desktop/subory/skladby.txt", "r")
lines = file.readlines()

x, y = 0, 0

for i in range(len(lines)):

    x += int(lines[i][10:-1].split(":")[0])
    y += int(lines[i][10:-1].split(":")[1])

x += y//60
y = y % 60

print(f"Total time: {x} minutes and {y} seconds")

################################################################
ffile = open("C:/Users/skola/Desktop/subory/pracdoba.txt")
llines = ffile.readlines()
final = []
for i in range(len(llines)):
    x1, x2 = llines[i].strip("\n").split(" ")[1].split(":")
    y1, y2 = llines[i].strip("\n").split(" ")[2].split(":")

    if x2 > y2:
        final.append(f"{int(y1) - int(x1)}:{60 - int(x2) + int(y2)}")
    else:
        final.append(f"{int(y1) - int(x1)}:{int(y2) - int(x2)}")

final






