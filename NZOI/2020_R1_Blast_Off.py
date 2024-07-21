r, n, t = map(int, input().split())
rockets = []
starts = []

for i in range(r):
    rocket = list(map(int, input().split()))
    rockets.append(rocket)

for i in range(n):
    starts.append(int(input()))

q = [0]
costs = [-1] * t
costs[0] = 0

while q:
    p = q.pop(0)
    cost = costs[p]
    for c, f in rockets:
        newcost = cost + c
        newp = p + f
        if newp < t and (costs[newp] == -1 or newcost < costs[newp]):
            costs[newp] = newcost
            q.append(newp)
        newp = abs(p - f)
        if newp < t and (costs[newp] == -1 or newcost < costs[newp]):
            costs[newp] = newcost
            q.append(newp)

for start in starts:
    print(costs[start])
