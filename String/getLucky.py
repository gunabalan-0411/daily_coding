class Solution:
    def getLucky(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        digits = [int(num) for num in 
        ''.join([str(abs(ord('a') - ord(ch))+1) for ch in s])
        ]
        ans = sum(digits)
    
        i = 1
        while i < k:
            ans = sum([int(ch) for ch in str(ans)])
            i += 1
        return ans