'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
	Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

	Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

	Example 1:

	Given nums = [1,1,2],

	Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

	It doesn't matter what you leave beyond the returned length.

'''
def removeDuplicates(nums) -> int:
    l = 1
    # We are always compare the current and prev values for duplication
    # Because since it non-decreasing order, its easy to find
    
    for r in range(1, len(nums)):
        # whenever we find a unique value we place it to l pointer (left most)
        # and increase the pointer
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l
nums = [0,1,1,1,2,2,2,2,4,4,4]
print(removeDuplicates(nums))
print(nums)