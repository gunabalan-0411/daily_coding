'''
https://leetcode.com/problems/jump-game/description/
'''
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        # From reverse checking we can reach the start 
        # and change the goal per iteration
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        
