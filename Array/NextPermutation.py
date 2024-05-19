'''
https://leetcode.com/problems/next-permutation/description/
'''
def nextPermutation(nums):
    # Step 1: find the decreasing sequence from the right
    index_i = len(nums) - 2 # to compare the items
    while index_i >= 0 and nums[index_i] >= nums[index_i+1]:
        index_i -= 1

    # Step 2: find the first highest num than this peak one from right
    if index_i >= 0:
        index_j = len(nums) - 1
        while index_j >= index_i and nums[index_j] <= nums[index_i]:
            index_j -= 1

        nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
    
    # Step 3: Sort the rem items after the peak
    start = index_i + 1
    end = len(nums) - 1
    
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

nums = [1,1,5]
nextPermutation(nums)
print(nums)