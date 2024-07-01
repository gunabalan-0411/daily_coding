class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows = len(matrix)
        # cols = len(matrix[0])
        # zero_rows = set()
        # zero_cols = set()

        # # First pass: find all zeros and mark their rows and columns
        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             zero_rows.add(i)
        #             zero_cols.add(j)

        # # Second pass: set the marked rows and columns to zero
        # for i in range(rows):
        #     for j in range(cols):
        #         if i in zero_rows or j in zero_cols:
        #             matrix[i][j] = 0
        # -- O(1) Space solution
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False
        # Trace the zeros
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    # If we save 0 in 0,0 it could also makes the 0th column
                    # to be zero
                    else:
                        rowZero = True
        # Fill zeros except 0,0 rows and cols
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        # fill zeros in first rows if
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0