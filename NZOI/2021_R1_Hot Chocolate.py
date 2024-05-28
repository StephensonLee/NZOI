L, R = map(int, input().split())
N = int(input())
students = []
cups = [0]
for i in range(N):
    # [c, l, r]
    students.append(list(map(int, input().split())))
    cups.append(cups[-1] + students[-1][0])

dp = [[None] * (L + 1) for i in range(N + 1)]


def solve(dp, id, l):
    if id >= N:
        return 0
    if dp[id][l] != None:
        return dp[id][l]

    ci, li, ri = students[id]
    r = cups[id] - l
    dp[id][l] = -9999999999
    if l + ci <= L and li > 0:
        dp[id][l] = max(dp[id][l], li + solve(dp, id + 1, l + ci))
    if r + ci <= R and ri > 0:
        dp[id][l] = max(dp[id][l], ri + solve(dp, id + 1, l))

    return dp[id][l]


ans = solve(dp, 0, 0)
if ans < 0:
    print('Camp is cancelled')
else:
    print(ans)
