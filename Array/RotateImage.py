'''
https://leetcode.com/problems/rotate-image/
'''
def rotate(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        # no of col - 1 shifts will happen for every layer
        for i in range(right - left):
            top, bottom = left, right

            top_left_cache = matrix[top][left+i]

            # -- Reverse swapping
            # Think about the movement for each layer to guess where to put i
            matrix[top][left+i] = matrix[bottom-i][left]

            matrix[bottom-i][left] = matrix[bottom][right-i]

            matrix[bottom][right-i] = matrix[top+i][right]

            matrix[top+i][right] = top_left_cache
        
        left += 1
        right -= 1




