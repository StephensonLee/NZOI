nums = input()

count = 0
n = len(nums)
for i in range(n):
    digit = int(nums[i])
    if nums[:i] != '':
        left = int(nums[:i])
    else:
        left = 0
    if nums[i + 1:] != '':
        right = int(nums[i + 1:])
    else:
        right = 0
    if digit < 3:
        count += left * 10 ** (n - i - 1)
    elif digit == 3:
        count += left * 10 ** (n - i - 1) + (right + 1)
    else:
        count += (left + 1) * 10 ** (n - i - 1)
print(count)
