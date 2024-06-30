class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i, ch in enumerate(s[::-1]):
            s[i] = ch