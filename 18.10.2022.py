import random as rn
import time

start = time.time()
points = 0

for i in range(10):

    x, y = rn.randint(1, 10), rn.randint(1, 10)
    sol = x * y

    ans = int(input(f"What is {x} * {y}"))

    if ans == sol:
        points += 3

    elif int(input("Try again")) == sol:
        points += 2

    elif int(input("Try again")) == sol:
        points += 1

    else:
        print("You failed")

end = time.time()

print(f"Your score is {points}/30 which is {round((points / 30) * 100)}%")
print(f"Your time was {end - start}")
