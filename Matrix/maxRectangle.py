from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [[int(item) for item in row] for row in matrix]
        max_rectangle = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
                elif i > 0 and matrix[i][j] == 0:
                    matrix[i][j] = 0
            max_rectangle = max(max_rectangle, self.maxHistogramRectangle(matrix[i]))
        return max_rectangle

    def maxHistogramRectangle(self, heights: List[int]) -> int:
        max_re = 0
        stack = [] # (index, height)
        # Iterate 1: left to right
        # remove heights that are not going extend until the next heights
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_re = max(max_re, height * (i-index))
                start = index
            # if the current height is less the before height we can take that before
            # height's start index this index as it can includes this small height.
            stack.append((start, h))
        
        # Iterate 2: right to left (since using stack)
        for i, h in stack:
            max_re = max(max_re, h * (len(heights) - i))
        return max_re 
        


        