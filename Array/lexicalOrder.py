from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(int, sorted(list(map(str, range(1,n+1))))))
        