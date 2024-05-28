n, d = map(int, input().split())
kps = {}
ks = []

for i in range(d):
    k, p = map(int, input().split())
    if k in kps:
        kps[k].append(p)
    else:
        ks.append(k)
        kps[k] = [p]

maps = []
for i in range(50):
    mapi = [0] * (i + 1)
    maps.append(mapi)

ks.sort()
ki = 0
ans = []
for i in range(n):
    if ki < len(ks):
        k = ks[ki]
        if k == i + 1:
            ps = kps[k]
            for p in ps:
                maps[p - 1][k % p] += 1
            ki += 1
    count = 0
    for p in range(50):
        count += maps[p][(i + 1) % (p + 1)]
    if count % 2 == 1:
        print('ON')
    else:
        print('OFF')
