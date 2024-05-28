## Important Questions
#### Two Sum - `Array`

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

<b>Example 1:</b>
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```python
class Solution:
    def twoSum(self, nums, target):
        # Value - Index Pair
        mapping = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in mapping:
                return [index, mapping[diff]]
            mapping[value] = index
```
---
