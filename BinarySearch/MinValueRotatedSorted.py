'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''
def findMin(nums):
    # 32 ms
    # return min(nums)
    # 38 ms
    minVal = nums[0]
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        minVal = min(minVal, nums[mid])
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return minVal