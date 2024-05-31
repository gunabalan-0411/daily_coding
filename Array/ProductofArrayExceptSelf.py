'''
https://leetcode.com/problems/product-of-array-except-self/
'''
def productExceptSelf(nums):
    # My solution: 252 ms
    # result = []
    # whole_product = math.prod(nums)
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         result.append(whole_product // nums[i])
    #     else:
    #         result.append(math.prod(nums[:i]+nums[i+1:]))
    # return result

    # Efficient solution 273ms
    #           1, 2, 3, 4
    # Prefix:   1, 2, 6, 24    Multiply each result with next element from left  
    # Postfix:  24, 24, 12, 4  Multiply each result with next element from right
    # Output:   24, 12, 8, 6   Multiply the element before and after
    # Now Instead of having two arrays, use two for loops
    # to store the prev multiplies on each element and again multiply it with 
    # post multiplies from last
    
    res = [1] * len(nums) # Creating the output array with 1

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for j in range(len(nums)-1, -1, -1):
        res[j] *= postfix
        postfix *= nums[j]
    
    return res