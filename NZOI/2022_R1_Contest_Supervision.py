R, C = map(int, input().split())
N = int(input())
cords = []
for i in range(N):
    r, c = map(int, input().split())
    cords.append([r, c])

crmap = {}
for r, c in cords:
    if c not in crmap:
        crmap[c] = r
    elif r > crmap[c]:
        crmap[c] = r


def furthest(x):
    dis_max = 0
    c_max = C
    for c, r in crmap.items():
        dis = (x - c) ** 2 + r ** 2
        if dis > dis_max or (dis == dis_max and c < c_max):
            dis_max = dis
            c_max = c
    return dis_max, c_max


lower = min(crmap)
upper = max(crmap)

while lower < upper - 1:
    mid = (lower + upper) // 2
    _, c_mid = furthest(mid)
    if c_mid < mid:
        upper = mid
    elif c_mid > mid:
        lower = mid
    else:
        lower = upper = mid

dis_lower, _ = furthest(lower)
dis_upper, _ = furthest(upper)
if dis_lower <= dis_upper:
    print(lower)
else:
    print(upper)
