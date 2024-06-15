class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # add all top rows elements
            for i in range(left, right):
                output.append(matrix[top][i])
            # top row onboarded
            top += 1
            # add all top to bottom elements
            for i in range(top, bottom):
                output.append(matrix[i][right-1]) # right is actual length 
            # right most onboarded
            right -= 1
            # Edge case where single col or single row
            if not (left < right and top < bottom):
                break
            # add all right to left elements
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i]) # bottom is also actual length
            # bottom row onboarded
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][left])
            # left most row onboarded
            left += 1
        return output