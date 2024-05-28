from heapq import heappush, heappop
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

n, d = map(int, input().split())
adj = [[] for i in range(n)]
compromise = []

for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(d):
    compromise.append(int(input()))

bn = len(adj[0])
depths = [[] for i in range(bn)]
branch = [-1 for i in range(n)]
deleted = set()


def bfs(b):
    bfs = [b]
    idx = adj[0].index(b)
    depth = -1
    while len(bfs) > 0:
        nextbfs = []
        for n in bfs:
            heappush(depths[idx], (depth, n))
            for m in adj[n]:
                branch[m] = b
                adj[m].remove(n)
                nextbfs.append(m)
        depth -= 1
        bfs = nextbfs


for b in adj[0]:
    branch[b] = b
    adj[b].remove(0)
    bfs(b)


def update_bfs(i):
    q = deque()
    q.append(i)
    while q:
        n = q.popleft()
        deleted.add(n)
        for m in adj[n]:
            if m not in deleted:
                q.append(m)


def max_loop():
    ls = []
    for b in adj[0]:
        if b not in deleted:
            idx = adj[0].index(b)
            while depths[idx][0][1] in deleted:
                heappop(depths[idx])
            heappush(ls, depths[idx][0][0])
    if len(ls) == 0:
        return 1
    elif len(ls) == 1:
        return -ls[0] + 1
    else:
        max1 = ls[0]
        heappop(ls)
        max2 = ls[0]
        return -max1 - max2 + 1


print(max_loop())
for c in compromise:
    update_bfs(c)
    print(max_loop())
