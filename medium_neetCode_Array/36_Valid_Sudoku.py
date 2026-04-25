import collections

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def validSudoku(board):

    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            square_keys = (r//3, c//3)
            if (val in rows[r] or
                val in columns[c] or
                val in squares[square_keys]):
                return False
            rows[r].add(val)
            columns[c].add(val)
            squares[square_keys].add(val)
    return True

print(validSudoku(board))