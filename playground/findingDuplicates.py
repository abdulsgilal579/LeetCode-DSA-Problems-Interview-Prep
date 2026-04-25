import collections
from multiprocessing.reduction import duplicate

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","."],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# def duplicateInRows(board):
#     rows = collections.defaultdict(set)
#     for r in range(9):
#         for c in range(9):
#             val = board[r][c]
#             if val == ".":
#                 continue
#             if val in rows[r]:
#                 return False
#             rows[r].add(val)
#     return True

# def duplicateInColumns(board):
#     columns = collections.defaultdict(set)
#     for r in range(9):
#         for c in range(9):
#             val = board[r][c]
#             if val == ".":
#                 continue
#             if val in columns[c]:
#                 return False
#             columns[c].add(val)
#     return True

# print(duplicateInRows(board))

def duplicateInBoxes(board):
    boxes = collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            box_key = (r//3, c//3)
            if val in boxes[box_key]:
                return False
            boxes[box_key].add(val)
    return True



