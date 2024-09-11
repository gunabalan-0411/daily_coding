class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while goal > 0 or start > 0:
            print(bin(goal))
            print(bin(start))
            if (start & 1) != (goal & 1):
                count += 1
            goal = goal >> 1
            start = start >> 1
            
        return count

# 1010
# 0111
print(Solution().minBitFlips(10, 7))