mean = 2
maximum = 3

if mean <= 1.5 and maximum <= 2:
    print("vyznamenanie")

elif mean <= 2 and maximum <= 3:
    print("velmi dobre")

elif maximum <= 4:
    print("prospel")

else:
    print("neprospel")

# new problem
# gardes

grades = []

grades.append(int(input("Enter the grade")))

while 0 not in grades:
    grades.append(int(input("Enter the grade")))

average = sum(grades[:-1]) / len(grades)


def max_grade(grades):
    big = grades[0]
    for i in range(len(grades)):
        if grades[i] > big:
            big = grades[i]

    return big


def min_grade(grades):
    smol = grades[0]
    for i in range(len(grades[:-1])):
        if grades[i] < smol:
            smol = grades[i]

    return smol


min_grade(grades)

# new problem

grades = []

grades.append(int(input("Enter the grade")))

while 0 not in grades:
    grades.append(int(input("Enter the grade")))

average = sum(grades[:-1]) / len(grades)

max_grade(grades)

if average <= 1.5 and max_grade(grades) <= 2:
    print("vyznamenanie")

elif average <= 2 and max_grade(grades) <= 3:
    print("velmi dobre")

elif max_grade(grades) <= 4:
    print("prospel")

else:
    print("neprospel")




























