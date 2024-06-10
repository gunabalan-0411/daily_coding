class Solution:
    def restoreString(self, s: str, indices) -> str:
        l = len(s)
        shuffle = "_" * l
        for i in range(l):
            shuffle = shuffle[:indices[i]] + s[i] + shuffle[indices[i]+1:]
        return shuffle