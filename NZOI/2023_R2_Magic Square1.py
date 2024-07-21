import sys

sys.setrecursionlimit(10 ** 6)

board = [list(map(int, input().split())) for i in range(3)]


def find_zeros():
    counts = [0] * 8
    for i in range(3):
        counts[i] = board[i].count(0)
    for i in range(3):
        counts[i + 3] = [board[0][i], board[1][i], board[2][i]].count(0)
    counts[6] = [board[0][0], board[1][1], board[2][2]].count(0)
    counts[7] = [board[0][2], board[1][1], board[2][0]].count(0)
    return counts


def find_total(r, c):
    if board[r][c] <= 0:
        return -1
    totals = [0] * 4
    if 0 not in board[r]:
        totals[0] = sum(board[r])
    if 0 not in [board[0][c], board[1][c], board[2][c]]:
        totals[1] = board[0][c] + board[1][c] + board[2][c]
    if r == c and 0 not in [board[0][0], board[1][1], board[2][2]]:
        totals[2] = board[0][0] + board[1][1] + board[2][2]
    if r + c == 2 and 0 not in [board[0][2], board[1][1], board[2][0]]:
        totals[3] = board[0][2] + board[1][1] + board[2][0]
    ans = max(totals)
    for total in totals:
        if total > 0 and total != ans:
            return -1
    return ans


def solve(board, total):
    counts = find_zeros()
    if 1 in counts:
        ind = counts.index(1)
    elif 2 in counts:
        ind = counts.index(2)
    else:
        return True

    if ind < 3:
        r = ind
        c = board[ind].index(0)
    elif ind < 6:
        c = ind - 3
        r = [board[0][c], board[1][c], board[2][c]].index(0)
    elif ind == 6:
        r = [board[0][0], board[1][1], board[2][2]].index(0)
        c = r
    else:
        r = [board[0][2], board[1][1], board[2][0]].index(0)
        c = 2 - r

    if total > 0 and 1 in counts:
        if ind < 3:
            board[r][c] = total - sum(board[ind])
        else:
            board[r][c] = total - board[0][c] - board[1][c] - board[2][c]
        if find_total(r, c) == total and solve(board, total):
            return True
        else:
            board[r][c] = 0
    else:
        for i in range(1, 10001):
            board[r][c] = i
            check = find_total(r, c)
            if check > 0:
                total = check
            if check >= 0 and solve(board, total):
                return True
            else:
                board[r][c] = 0
    return False


total = 0
counts = find_zeros()
if 0 in counts:
    ind = counts.index(0)
    if ind < 3:
        total = sum(board[ind])
    elif ind < 6:
        total = board[0][ind - 3] + board[1][ind - 3] + board[2][ind - 3]
    elif ind == 6:
        total = board[0][0] + board[1][1] + board[2][2]
    else:
        total = board[0][2] + board[1][1] + board[2][0]

solve(board, total)
for row in board:
    for n in row:
        print(n, end=' ')
    print()
