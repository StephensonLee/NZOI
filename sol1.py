import heapq
import sys

sys.setrecursionlimit(10 ** 6)

N, D = map(int, input().split())
adj = [[] for i in range(N)]
rooted_adj = [[] for i in range(N)]
depths_nodes = []
deleted = set()

for i in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def root_and_find_depths(cur, parent, adj_list, rooted_adj, depth):
    heapq.heappush(depths_nodes, (-depth, cur))

    for neighbour in adj[cur]:
        if neighbour != parent:
            rooted_adj[cur].append(neighbour)
            root_and_find_depths(neighbour, cur, adj_list, rooted_adj, depth + 1)


def delete_node(cur, rooted_adj, deleted):
    deleted.add(cur)
    for neighbour in rooted_adj[cur]:
        if neighbour not in deleted:
            delete_node(neighbour, rooted_adj, deleted)


root_and_find_depths(0, -1, adj, rooted_adj, 0)

print(-depths_nodes[0][0] + 1)

for i in range(D):
    k = int(input())
    delete_node(k, rooted_adj, deleted)
    while (depths_nodes[0][1] in deleted):
        heapq.heappop(depths_nodes)
    print(-depths_nodes[0][0] + 1)
