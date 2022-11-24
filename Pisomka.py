import random as rn

tips = []
nums = []

for i in range(6):
    tips.append(int(input("Enter your tips ranging from 1 to 10")))

while len(nums) != len(tips):

    x = rn.randint(1, 10)

    if x not in nums:
        nums.append(x)

score = 0
guessed_nums = []
for i in range(len(tips)):
    if tips[i] in nums:
        score += 1
        guessed_nums.append(tips[i])

print(f"You have {score} good guesses which are {sorted(guessed_nums)}")
