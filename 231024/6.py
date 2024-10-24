nums = []
while (n := int(input())) != 0:
    nums.append(n)

nums.sort()
print(nums[-1] + nums[-2])
print(nums[0] + nums[1])
