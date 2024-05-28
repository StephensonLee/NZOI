n = int(input())
cs = []
rs = []
for i in range(n):
    ci, ri = map(int, input().split())
    cs.append(ci)
    rs.append(ri)

rs.sort()
rr = rs[n // 2]
sumr = 0
for r in rs:
    sumr += abs(r - rr)

cs.sort()
cc = cs[n // 2]
sumc = 0
for c in cs:
    sumc += abs(c - cc)

print(min(sumc, sumr))
