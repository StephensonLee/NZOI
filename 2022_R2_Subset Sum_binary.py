from math import log2

n = int(input())
numsa = list(map(int, input().split()))
numsb = list(map(int, input().split()))

suma = [False] * 33
counta = [0] * 16
sumb = [False] * 33
countb = [0] * 16
for num in numsa:
    ind = int(log2(num))
    counta[ind] += 1
    while suma[ind] == True:
        ind += 1
    suma[ind] = True

for num in numsb:
    ind = int(log2(num))
    countb[ind] += 1
    while sumb[ind] == True:
        ind += 1
    sumb[ind] = True

ind = 0
while ind < 34:
    if suma[ind] and sumb[ind]:
        break
    ind += 1

ansa = []
count = 1
ai = ind
while count > 0:
    if counta[ai] >= count:
        for i in range(count):
            ansa.append(2 ** (ai))
        break
    else:
        for i in range(counta[ai]):
            ansa.append(2 ** (ai))
        count -= counta[ai]
        count *= 2
        ai -= 1

ansb = []
count = 1
bi = ind
while count > 0:
    if countb[ind] >= count:
        for i in range(count):
            ansb.append(2 ** (bi))
        break
    else:
        for i in range(countb[bi]):
            ansb.append(2 ** (bi))
        count -= countb[bi]
        count *= 2
        bi -= 1

for num in ansa:
    print(num, end=' ')
print()
for num in ansb:
    print(num, end=' ')
