board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"


def solve(r, c, i):
    if i == len(word) - 1 and board[r][c] == word[i]:
        return True
    if board[r][c] == word[i]:
        used[r][c] = True
        if r - 1 >= 0 and not used[r - 1][c] and solve(r - 1, c, i + 1):
            return True
        elif r + 1 < len(board) and not used[r + 1][c] and solve(r + 1, c, i + 1):
            return True
        elif c - 1 >= 0 and not used[r][c - 1] and solve(r, c - 1, i + 1):
            return True
        elif c + 1 < len(board[0]) and not used[r][c + 1] and solve(r, c + 1, i + 1):
            return True
        used[r][c] = False
    return False


found = False
used = [[False] * len(board[0]) for i in range(len(board))]
for r in range(len(board)):
    for c in range(len(board[0])):
        if solve(r, c, 0):
            found = True
            break
print(found)
