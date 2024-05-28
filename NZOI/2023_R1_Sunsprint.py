from collections import deque

intense, t = map(int, input().split())
st = list(map(int, input().split()))
n, m = map(int, input().split())
neibour = {}
for i in range(m):
    a, b, d, s = input().split()
    a, b, d = map(int, (a, b, d))
    if a in neibour:
        neibour[a].append([b, d, s])
    else:
        neibour[a] = [[b, d, s]]

q = deque()
q.append(0)
suns = [[10 ** 6] for i in range(n)]
suns[0] = [0] * (t + 1)

while q:
    cur = q.popleft()
    if cur in neibour:
        neibs = neibour[cur]
        suna = suns[cur]
        for b, d, s in neibs:
            update = False
            sunb = suns[b]
            minb = min(sunb)
            if s == 'S':
                cur_i = 0
            else:
                cur_i = intense
            for i in range(len(suna) + d - len(sunb)):
                sunb.append(minb)
            for i in range(len(suna)):
                if i + d < t:
                    sun = suna[i] + sum(st[i:i + d])
                elif i < t:
                    sun = suna[i] + sum(st[i:]) + (i + d - t) * cur_i
                else:
                    sun = suna[i] + d * cur_i

                if sun < minb:
                    update = True
                    minb = sun
                sunb[i + d] = minb
            for i in range(len(suna) - 1 + d, len(sunb)):
                if sunb[i] > minb:
                    sunb[i] = minb
            if update and b not in q:
                q.append(b)

print(min(suns[-1]))
