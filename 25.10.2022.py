salary, nums = 8000, [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
for i in range(len(nums)):
    if salary // nums[i] >= 0:
        print(f"{salary // nums[i]} * {nums[i]}")
        salary -= (salary // nums[i]) * nums[i]
#############################################################
date = "12.13.2012"
day, month, year = date.split(".")
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if int(month) > 12 or int(day) > months[int(month)]:print("Wrong")
else:
    days = 0
    days += months[int(month)] - int(day)
    for i in range(int(month), len(months)):days += months[i]
#############################################################
