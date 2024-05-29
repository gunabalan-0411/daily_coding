'''
https://leetcode.com/problems/valid-sudoku/description/
'''
import collections

def isValidSudoku(board):
    # We just validating the question(if unique in all directions)
    # not whether it could be solvable

    # Hash set
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    # We should compare the values with outside of this sub matrix
    square = collections.defaultdict(set) # keys: (r//3, c//3)

    for r in range(9):
        for c in range(9):
            # Shouldn't care about the empty cells
            if board[r][c] == '.':
                continue

            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in square[(r//3, c//3)]):
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            square[(r//3, c//3)].add(board[r][c])

    return True
