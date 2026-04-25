import collections

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


#Solution With Extra Prints
# def isValidSudoku(board):
#     cols    = collections.defaultdict(set)
#     rows    = collections.defaultdict(set)
#     squares = collections.defaultdict(set)  # key = (r//3, c//3)
#
#     for r in range(9):
#         for c in range(9):
#
#             val = board[r][c]
#
#             # skip empty cells
#             if val == ".":
#                 continue
#
#             box_key = (r // 3, c // 3)
#
#             print(f"\n--- Cell ({r},{c}) = '{val}' | box={box_key} ---")
#             print(f"  rows[{r}]        = {rows[r]}")
#             print(f"  cols[{c}]        = {cols[c]}")
#             print(f"  squares{box_key} = {squares[box_key]}")
#
#             # THE CHECK
#             if (val in rows[r] or
#                 val in cols[c] or
#                 val in squares[box_key]):
#                 print(f"  ❌ DUPLICATE FOUND → return False")
#                 return False
#
#             # record it
#             rows[r].add(val)
#             cols[c].add(val)
#             squares[box_key].add(val)
#             print(f"  ✅ No duplicate → added to all 3 sets")
#
#     print("\n✅ All cells checked — return True")
#     return True
#
#
# result = isValidSudoku(board)
# print(f"\nFinal answer: {result}")

#Real Solution
def isValidSudoku(board):
    cols    = collections.defaultdict(set)
    rows    = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == ".":
                continue

            box_key = (r // 3, c // 3)

            if (val in rows[r] or
                val in cols[c] or
                val in squares[box_key]):
                return False

            rows[r].add(val)
            cols[c].add(val)
            squares[box_key].add(val)

    return True

result = isValidSudoku(board)
print(result)