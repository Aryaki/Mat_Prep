# check if the parentheses are correct

x = "(())()())"

left = 0
right = 0

for i in range(len(x)):
    if x[i] == "(":
        left += 1

        if left < right:
            print("Wrong")
            break

    elif x[i] == ")":
        right += 1

        if left < right:
            print("Wrong")
            break

if left > right:
    print("wrong")
