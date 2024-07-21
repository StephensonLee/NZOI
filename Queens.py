def solveNQueens(n: int):
    digsum = []
    digdiff = []
    ans = []

    def solve(board):
        if len(board) == n:
            result = []
            for num in board:
                rows = ''
                for col in range(n):
                    if col == num:
                        rows += 'Q'
                    else:
                        rows += '.'
                result.append(rows)
            ans.append(result)

        for col in range(n):
            row = len(board)
            if col not in board and row + col not in digsum and row - col not in digdiff:
                board.append(col)
                digsum.append(row + col)
                digdiff.append(row - col)
                solve(board)
                board.pop()
                digsum.pop()
                digdiff.pop()

    solve([])
    return ans


print(solveNQueens(8))
