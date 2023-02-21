num = 1179
sus = 16

ans = []

while num != 0:
    ans.append(num % sus)
    num = num//sus

alpha = ["A", "B", "C", "D", "E", "F"]

out = []

for i in range(len(ans), 0, -1):
    if ans[i - 1] >= 10:
        out.append(alpha[ans[i-1] - 10])

    else:
        out.append(ans[i-1])

print(out)

#########################################################################

x = "4D"
sust = 4
output = 0

for i in range(len(x)):
    if x[i] in alpha:
        output+=(alpha.index(x) + 10) * 4

    else:
        output += x

















