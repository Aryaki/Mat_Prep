
salary = 1843

nums = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
output = []

for i in range(len(nums)):
    if salary // nums[i] >= 0:
        output.append(f"{salary // nums[i]} * {nums[i]}")
        salary = (salary // nums[i]) * nums[i]
