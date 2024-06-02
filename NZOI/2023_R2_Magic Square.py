board = [list(map(int, input().split())) for i in range(3)]


def find_zero(r, c):
    countr = 0
    for i in range(3):
        if board[r][i] == 0:
            countr += 1
    countc = 0
    for i in range(3):
        if board[i][c] == 0:
            countc += 1
    return countr, countc


def pick():
    count = 3
    r = -1
    c = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                cur = min(find_zero(i, j))
                if cur < count:
                    count = cur
                    r, c = i, j
    return r, c


def check():
    total = -1
    for i in range(3):
        if board[i][0] != 0 and board[i][1] != 0 and board[i][2] != 0:
            totalr = board[i][0] + board[i][1] + board[i][2]
            if total == -1:
                total = totalr
            elif total != totalr:
                return False
    for i in range(3):
        if board[0][i] != 0 and board[1][i] != 0 and board[2][i] != 0:
            totalc = board[0][i] + board[1][i] + board[2][i]
            if total == -1:
                total = totalc
            elif total != totalc:
                return False
    if board[0][0] != 0 and board[1][1] != 0 and board[2][2] != 0:
        totald1 = board[0][0] + board[1][1] + board[2][2]
        if total == -1:
            total = totald1
        elif total != totald1:
            return False
    if board[0][2] != 0 and board[1][1] != 0 and board[2][0] != 0:
        totald2 = board[0][2] + board[1][1] + board[2][0]
        if total == -1:
            total = totald2
        elif total != totald2:
            return False
    return True


def solve():
    r, c = pick()
    if r == -1:
        return True
    else:
        for i in range(1, 10001):
            board[r][c] = i
            if check():
                if solve():
                    return True
            else:
                board[r][c] = 0
    return False


solve()
for row in board:
    for n in row:
        print(n, end=' ')
    print()
