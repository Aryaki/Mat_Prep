day = 1
month = 1
year = 2022

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month > 12 or day > days[month - 1]:
    print("Invalid month")

result = 0

result += days[month - 1] - day

for i in range(month, month + len(days) - month):
    result += days[i]

################################################################
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



















