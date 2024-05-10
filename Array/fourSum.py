'''
https://leetcode.com/problems/4sum/description/
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order. 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''
def fourSum(nums, target):
    nums.sort()
    result, stack = [], []
    # Target will also get reduced along recursion because, permutation of numbers will be reduced from target
    # so that at base case: we can simply use l and r index values to check if they equal to target
    def kSum(k, start, target):
        # For K = 2 we don't need a for loop, we only need a while loop and for others we need K - 2 for loops.
        if k != 2:
            # Reducing the iteraction by k because we need unique positions of k variables in the array
            for i in range(start, len(nums) - k + 1):
                # To avoid duplicate iteration, to avoid error i - 1 we are using i > start
                if i > start and nums[i] == nums[i - 1]:
                    continue
                stack.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                stack.pop()
            return
        
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                result.append(stack + [nums[l], nums[r]])
                # To exit loop we need to get forward
                l += 1
                # To avoid duplicate numbers
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    kSum(4, 0, target)
    return result

print(fourSum([1,0,-1,0,-2,2], 0))