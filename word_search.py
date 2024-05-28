def exist(board, word):
    def search(i, r, c):
        if word[i] == board[r][c]:
            if i == len(word) - 1:
                return True
            else:
                used[r][c] = True
                if r + 1 < len(board) and not used[r + 1][c] and search(i + 1, r + 1, c):
                    return True
                elif r - 1 >= 0 and not used[r - 1][c] and search(i + 1, r - 1, c):
                    return True
                elif c + 1 < len(board[0]) and not used[r][c + 1] and search(i + 1, r, c + 1):
                    return True
                elif c - 1 >= 0 and not used[r][c - 1] and search(i + 1, r, c - 1):
                    return True
                used[r][c] = False
        return False

    used = [[False] * len(board[0]) for i in range(len(board))]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if search(0, r, c):
                return True

    return False


board = [["a"]]
word = "a"
print(exist(board, word))
