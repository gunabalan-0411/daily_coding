class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        path = set()
        def dfs(r, c, i):
            # Positive Exit case
            if i == len(word):
                return True
            # Negative Exit case
            if (
                # Out of bounds case
                r < 0 or c < 0 or
                r >= ROW or c >= COL or
                # Chars not match
                board[r][c] != word[i] or
                # Duplicate path
                (r, c) in path):
                return False

            path.add((r, c))
            res = (
                dfs(r, c-1, i+1) or #move left
                dfs(r, c+1, i+1) or #move right
                dfs(r-1, c, i+1) or #move up
                dfs(r+1, c, i+1)    #move down
            )
            path.remove((r, c))
            return res
        # For each char as start position
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0): return True
        return False

        