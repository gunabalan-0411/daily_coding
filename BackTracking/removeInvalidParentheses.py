from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = set()
        self.longest_str = -1
        self.dfs(s, 0, [], 0, 0)
        return list(self.res)