'''
https://leetcode.com/problems/count-and-say/
'''
def count_and_say(n):
    def counter(nums):
        count = 1
        result = ''
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] != nums[i+1]:
                result += str(count) + nums[i]
                count = 1
            else:
                count += 1
        return result
    
    ans = '1'
    for i in range(2, n+1):
        ans = counter(ans)
    return ans