ans = []


def dfs(cur, rest):
    global ans
    if not rest:
        ans.append(cur.copy())
    else:
        for i in range(len(rest)):
            num = rest[i]
            cur.append(num)
            rest.pop(i)
            dfs(cur, rest)
            cur.pop()
            rest.insert(i, num)


nums = [1, 2, 3]
dfs([], nums)

print(ans)
