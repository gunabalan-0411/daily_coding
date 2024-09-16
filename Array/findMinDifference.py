from typing import List
"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = 24*60
        nums = sorted(
                [
                int(timepoint[:2])*60 + int(timepoint[3:]) for timepoint in timePoints
            ]
        )
        for a, b in zip(nums, nums[1:]):
            ans = min(ans, b - a)

        return min(ans, 24*60-nums[-1] + nums[0])
    
timePoints = ["00:00","23:59","00:00"]
print(Solution().findMinDifference(timePoints))