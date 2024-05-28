import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
numsa = list(map(int, input().split()))
numsb = list(map(int, input().split()))
useda = [False] * len(numsa)
usedb = [False] * len(numsb)
found = False
numsa.sort()
numsb.sort()


def solve(num):
    if num > 0:
        used = usedb
        nums = numsb
    else:
        used = useda
        nums = numsa
    for i in range(n):
        if not used[i]:
            used[i] = True
            if num > 0:
                nextnum = num - nums[i]
            else:
                nextnum = num + nums[i]
            if nextnum == 0:
                return True
            if solve(nextnum):
                return True
            else:
                used[i] = False
    return False


solve(0)
for i in range(n):
    if useda[i]:
        print(numsa[i], end=' ')
print()
for i in range(n):
    if usedb[i]:
        print(numsb[i], end=' ')
