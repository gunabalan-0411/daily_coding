'''
https://leetcode.com/problems/missing-number/
'''
def missingNumber(nums) -> int:
    # -- 1455 ms my solution - 1
    # size = len(nums)
    # for i in range(size):
    #     if i not in nums:
    #         return i
    # return size
    # -- 115 ms my solution - 2
    # res = list(set(list(range(len(nums)))) - set(nums))
    # return res[0] if res else len(nums)
    # -- 114 ms O(2n)
    # return sum(list(range(len(nums)+1))) - sum(nums)
    # -- 106 ms similar to above method
    res = len(nums)
    for i in range(len(nums)):
        res += (i - nums[i])
    return res