n= 100

y = {0}
for i in range(n):
    y.add(i)
x2 = {0}
x3 = {0}
x5 = {0}

for i in range(n):
    if i//3 == 0:
        x3.add(i)

for i in range(n):
    if str(i)[-1] == "5":
        x5.add(i)

for i in range(n):
    if 2**i<n:
       x2.add(2**i)

#################################

