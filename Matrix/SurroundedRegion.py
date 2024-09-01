from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        def cover(r, c):
            if (r < 0 or r==ROW or c < 0 or c == COL or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            cover(r, c+1)
            cover(r, c-1)
            cover(r+1, c)
            cover(r-1, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O' and (r in [0, ROW-1] or c in [0, COL-1]):
                    cover(r, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
