n = int(input())
numsa = list(map(int, input().split()))
numsb = list(map(int, input().split()))


def update_sum(num, n):
    newsums = {}
    for sum in sums.keys():
        for i in range(1, n + 1):
            cur = sum + num * i
            # print(cur)
            if cur == 0:
                sums.update(newsums)
                return num
            if cur not in sums and cur not in newsums:
                newsums[cur] = num
    sums.update(newsums)
    return 0


sums = {0: 0}
last = 0
mapa = {}
mapb = {}
for a in numsa:
    if a in mapa:
        mapa[a] += 1
    else:
        mapa[a] = 1

for b in numsb:
    if b in mapb:
        mapb[b] += 1
    else:
        mapb[b] = 1

balance = 0
keya = sorted(list(mapa.keys()))
ai = 0
keyb = sorted(list(mapb.keys()))
bi = 0
last = 0
while last == 0 and (ai < len(keya) or bi < len(keyb)):
    if balance <= 0 or bi >= len(keyb):
        num = keya[ai]
        ai += 1
        last = update_sum(num, mapa[num])
        balance += num
    else:
        num = keyb[bi]
        bi += 1
        last = update_sum(-num, mapb[num])
        balance -= num

sa = []
sb = []

if last > 0:
    sa.append(last)
else:
    sb.append(-last)

cur = -last
while cur:
    if sums[cur] > 0:
        sa.append(sums[cur])
    else:
        sb.append(-sums[cur])
    cur -= sums[cur]

print(' '.join(map(str, sa)))
print(' '.join(map(str, sb)))
