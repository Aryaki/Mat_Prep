import math

# quadratic formula

a = 2
b = 4
c = 2


def q_formula(a, b, c):

    x1 = (-b + math.sqrt((b ** 2) - (4 * a * c)) / 2 * a)
    x2 = (-b - math.sqrt((b ** 2) - (4 * a * c)) / 2 * a)

    return x1, x2


try:

    x1, x2 = q_formula(a, b, c)

    if x1 != x2:
        print("2 korene")

    else:
        print("1 koren")

except:
    print("diskriminant je zaporny ")


# new problem
# triangle

a = 3
b = 2
c = 4

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("exists")

if a == b == c:
    print("rovnostranny")

elif a == b or a == c or b == c:
    print("rovnoramenny")

else:
    print("△")


















