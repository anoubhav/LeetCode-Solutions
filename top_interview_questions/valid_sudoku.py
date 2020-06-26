def validSudoku(board):
    # Case-wise solution. Check rows, columns and squares.
    # check rows
    for r in range(9):
        s = set()
        row = (''.join(board[r]))
        for char in row:
            if char!=".":
                if char in s:
                    return False
                else:
                    s.add(char)
    # check columns
    for c in range(9):
        s = set()
        for r in range(9):
            char = board[r][c]
            if char!=".":
                if char in s:
                    return False
                else:
                    s.add(char)
    # check boxes. Store all the left corners of each box
    left_corners = list(zip('0'*3 + '3'*3 + '6'*3, '036'*3))

    for lc in left_corners:
        row, col = map(int, lc)
        s = set()
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                char = board[r][c]
                if char!=".":
                    if char in s:
                        return False
                    else:
                        s.add(char)
    return True


def isvalid(i, j, c, seen):
    if ((c, j) not in seen) and ((i, c) not in seen) and ((i//3,j//3,c) not in seen):
        return True
    return False

def validSudoku_short(board):
    # iterates entire grid in one go. No separate cases.

    #  (i/3, j/3) identifies one of the nine 3x3 blocks.
    # why (c, j) but (i, c)? (the order of c, j, and i) --> To distinguish rows and columns, for example ('4', 4) and (4, '4'). This trick allows us to use a single set instead of separate sets for rows, columns, squares.

    seen = set()
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                if isvalid(i, j, c, seen):
                    seen.add((c, j))
                    seen.add((i, c))
                    seen.add((i//3,j//3,c))
                else:
                    return False
    return True

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(validSudoku(board))
print(validSudoku_short(board))