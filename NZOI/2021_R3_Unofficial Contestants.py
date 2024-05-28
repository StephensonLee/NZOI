from bisect import bisect_left

n = int(input())
M = int(input())
tos = []
nums = []
for i in range(M):
    to, num = input().split()
    num = int(num)
    tos.append(to)
    nums.append(num)

toggle = []
ans = []
for i in range(M):
    to = tos[i]
    num = nums[i]
    if to == 't':
        if len(toggle) == 0:
            toggle.append(num)
        else:
            left = bisect_left(toggle, num)
            if left == len(toggle) or toggle[left] != num:
                toggle.insert(left, num)
            else:
                del (toggle[left])

    else:
        if len(toggle) == 0:
            ans.append(num)
        else:
            left = bisect_left(toggle, num)
            if left == len(toggle) or toggle[left] != num:
                ans.append(num - left)
            else:
                ans.append('UNOFFICIAL')

for a in ans:
    print(a)
