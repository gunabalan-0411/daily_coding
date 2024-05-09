'''
    https://leetcode.com/problems/3sum-closest/
	Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
    Return the sum of the three integers. You may assume that each input would have exactly one solution.

	Example:

	Given array nums = [-1, 2, 1, -4], and target = 1.

	The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
# 345 ms
def threeSumClosest(nums, target) -> int:
        nums.sort()
        result, min_diff = 0, float('inf')
        size = len(nums)
        for index in range(size):
            left, right = index + 1, size - 1
            while left < right:
                cur_sum = nums[index] + nums[left] + nums[right]
                cur_diff = abs(target - cur_sum)

                if cur_diff == 0:
                    return target
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    result = cur_sum

                if cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
# 540 ms
def threeSumClosest(nums, target) -> int:
    nums.sort()
    size = len(nums)
    leftnearest_sum = float('-inf')
    rightnearest_sum = float('inf')
    for index in range(size):
        left, right = index + 1, size - 1
        while left < right:
            
            cur_sum = nums[index] + nums[left] + nums[right]
            if cur_sum <= target:
                leftnearest_sum = max(leftnearest_sum, cur_sum)
                left += 1
            elif cur_sum > target:
                rightnearest_sum = min(rightnearest_sum, cur_sum)
                right -= 1
                
    if target - leftnearest_sum < rightnearest_sum - target:
        return leftnearest_sum
    else:
        return rightnearest_sum
    