class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            # max frequency character in a window
            # using single variable (we always keep it the same or max)
            # because less maxf doesn't going to impact the res
            # - when maxf reduced res value will be same when the maxf is once 
            # - greater res is recorded with high value
            maxf = max(maxf, counts[s[r]])

            # Reduce the window size from left (also reduce char count)
            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

            