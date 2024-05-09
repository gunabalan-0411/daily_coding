'''
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''
def two_sum(nums, target):
    mapping = {}
    for index, value in enumerate(nums):
        difference = target - value
        if difference in mapping:
            return [index, mapping[difference]]
        else:
            mapping[value] = index
    # O(N)
# ----------------------------------------------------
print(two_sum([-3,2,3,91], 0))
    