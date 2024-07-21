board = []
n = 4
diff = []
summ = []


def check(r, c):
    if c in board:
        return False
    if r - c in diff:
        return False
    if r + c in summ:
        return False
    return True


def solve(r):
    global diff, summ
    if r == n:
        print(board)
    for c in range(n):
        if check(r, c):
            diff.append(r - c)
            summ.append(r + c)
            board.append(c)
            solve(r + 1)
            diff.pop()
            summ.pop()
            board.pop()


solve(0)
