from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        j = 1
        while j < numRows:
            temp = res[-1].copy()
            for i in range(1, len(temp)):
                temp[i] = res[-1][i] + res[-1][i-1]
            res.append(temp+[1])
            j += 1
        return res