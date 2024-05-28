connections = []
compromise = []

n, d = map(int, input().split())
for i in range(n - 1):
    a, b = map(int, input().split())
    connections.append([a, b])
for i in range(d):
    compromise.append(int(input()))


def bf(n, connections, compromise):
    tree = {}
    levels = {}
    prev = [-1] * n

    def generate_tree():
        for a, b in connections:
            if a in tree:
                tree[a].append(b)
            else:
                tree[a] = [b]
            if b in tree:
                tree[b].append(a)
            else:
                tree[b] = [a]
        bfs = [0]
        l = 0
        while len(bfs) > 0:
            nextbfs = []
            levels[l] = []
            for n in bfs:
                levels[l].append(n)
                for m in tree[n]:
                    tree[m].remove(n)
                    prev[m] = n
                    nextbfs.append(m)
            bfs = nextbfs
            l += 1

    generate_tree()

    lens = [1] * n

    def find_len():
        level = max(levels)
        while level >= 0:
            cur = levels[level]
            for n in cur:
                count = 1
                for m in tree[n]:
                    count = max(count, lens[m] + 1)
                lens[n] = count
            level -= 1

    find_len()

    def update_len(root):
        p = prev[root]
        prev[root] = -1
        tree[p].remove(root)
        while p != -1:
            count = 1
            for m in tree[p]:
                count = max(count, lens[m] + 1)
            lens[p] = count
            root = p
            p = prev[root]

    def max_loop():
        sublen = []
        for sub in tree[0]:
            sublen.append(lens[sub])
        sublen.sort(reverse=True)
        if len(sublen) == 0:
            return 1
        elif len(sublen) == 1:
            return sublen[0] + 1
        else:
            return sublen[0] + sublen[1] + 1

    ans = []
    ans.append(max_loop())
    for c in compromise:
        update_len(c)
        ans.append(max_loop())
    return ans
