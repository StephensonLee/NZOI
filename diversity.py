s = input()
nums = [int(x) for x in list(s)]
nums.insert(0, 0)
ind = len(nums) - 1
while ind >= 0:
    if nums[ind] == 10:
        nums[ind] = 0
        nums[ind - 1] += 1
    elif nums[ind] == nums[ind - 1] == 9:
        nums[ind] = 0
        nums[ind - 1] = 10
    ind -= 1

found = False
ind = 1
while ind < len(nums):
    if found:
        if nums[ind - 1] != 0:
            nums[ind] = 0
        else:
            nums[ind] = 1
    elif nums[ind] == nums[ind - 1]:
        found = True
        nums[ind] += 1
    ind += 1

if nums[0] == 0:
    nums.pop(0)

for i in nums:
    print(i, end='')
