class Solution:
    def greatestLetter(self, s: str) -> str:
        s = list(set(s))
        for c in range(26-1, -1, -1):
            ch = chr(ord('a')+c)

            if ch in s and ch.upper() in s:
                return ch.upper()
        return ''