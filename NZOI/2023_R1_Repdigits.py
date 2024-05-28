nums = list(map(int, input()))
ans = []
l = len(nums)
count = 0


def remove(i, digit):
    for ind in range(l - 1, i - 1, -1):
        if nums[ind] >= digit:
            nums[ind] -= digit
        else:
            nums[ind] = nums[ind] + 10 - digit
            nums[ind - 1] -= 1


def check(ind, digit):
    for i in range(ind, l):
        if nums[i] > digit:
            return True
        elif nums[i] < digit:
            return False
    return True


for i in range(l):
    if i > 0 and nums[i - 1] > 0:
        digit = 9
    elif i == l - 1 or check(i, nums[i]):
        digit = nums[i]
    else:
        digit = nums[i] - 1
    ans.append(digit)
    remove(i, digit)
    if digit != 0:
        count += 1

if nums[l - 1] != 0:
    print(count + 1)
    print(nums[l - 1])
else:
    print(count)

w = 1
for i in range(l - 1, -1, -1):
    if ans[i] != 0:
        print(ans[i] * w)
    w = 10 * w + 1
