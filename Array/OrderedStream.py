from typing import List
class OrderedStream:

    def __init__(self, n: int):
        self.s = [None] * n
        self.p = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.s[idKey-1] = value
        while self.p < len(self.s) and self.s[self.p]:
            self.p += 1
        return self.s[idKey-1: self.p]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)