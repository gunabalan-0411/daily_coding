from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        for i in range(rowIndex):
            post = pre.copy()
            for j in range(1, len(post)):
                post[j] = pre[j-1]+pre[j]
            pre = post[::] + [1]
        return pre



            