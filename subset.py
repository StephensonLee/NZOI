import sys
from math import log2, ceil

N = 100000
n = int(input())
numsa = list(map(int, input().split()))
numsb = list(map(int, input().split()))
dicta = {}
dictb = {}

for num in numsa:
    if num in dicta:
        dicta[num] += 1
    else:
        dicta[num] = 1

for num in numsb:
    if num in dictb:
        dictb[num] += 1
    else:
        dictb[num] = 1

if n <= 8:
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

elif len(dicta) == 1:
    numa = numsa[0]
    counta = dicta[numa]
    numb = numsb[0]
    countb = dictb[numb]
    found = False
    ansa = 0
    ansb = 0
    while not found:
        ansa += 1
        if (numa * ansa) % numb == 0:
            ansb = (numa * ansa) // numb
            found = True
    for i in range(ansa):
        print(numa, end=' ')
    print()
    for i in range(ansb):
        print(numb, end=' ')
    print()
else:
    counta2 = [0] * ceil(log2(N * N))
    countb2 = [0] * ceil(log2(N * N))

    for num in numsa:
        ind = int(log2(num))
        counta2[ind] += 1

    for num in numsb:
        ind = int(log2(num))
        countb2[ind] += 1

    sumsa = counta2.copy()
    for i in range(len(sumsa)):
        while sumsa[i] >= 2:
            sumsa[i + 1] += 1
            sumsa[i] -= 2
            if sumsa[i] == 0:
                sumsa[i] = 1

    sumsb = countb2.copy()
    for i in range(len(sumsb)):
        while sumsb[i] >= 2:
            sumsb[i + 1] += 1
            sumsb[i] -= 2
            if sumsb[i] == 0:
                sumsb[i] = 1

    ind = 0
    for i in range(len(sumsa)):
        if sumsa[i] == sumsb[i] == 1:
            ind = i
            break

    ansa = []
    count = 1
    inda = ind
    while count > 0:
        if inda >= len(counta2):
            count *= 2
            inda -= 1
        elif counta2[inda] >= count:
            for i in range(count):
                ansa.append(2 ** (inda))
            count = 0
        else:
            for i in range(counta2[inda]):
                ansa.append(2 ** (inda))
            count = (count - counta2[inda]) * 2
            inda -= 1

    ansb = []
    count = 1
    while count > 0:
        if ind >= len(countb2):
            count *= 2
            ind -= 1
        elif countb2[ind] >= count:
            for i in range(count):
                ansb.append(2 ** (ind))
            count = 0
        else:
            for i in range(countb2[ind]):
                ansb.append(2 ** (ind))
            count = (count - countb2[ind]) * 2
            ind -= 1

    for i in ansa:
        print(i, end=' ')
    print()
    for i in ansb:
        print(i, end=' ')
    print()
