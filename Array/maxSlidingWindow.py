from typing import List
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        q = collections.deque()
        output = []
        while r < len(nums):
            # Removing small vals to keep decreasing queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # Remove outofbounds values
            if l > q[0]:
                q.popleft()
            # Adding to output
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

        
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
# Output: [3,3,5,5,6,7]
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7