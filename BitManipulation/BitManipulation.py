'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit 
integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
'''
import math
def reverse_integer(x):
    # https://leetcode.com/problems/reverse-integer/
    # MAX_VAL = 2147483647
    # MIN_VAL = -2147483648
    # 22 ms
    MAX_VAL = (2 ** 31 ) - 1
    MIN_VAL = -2 ** 31
    res = 0
    while x:
        digit = int(math.fmod(x, 10)) # python dump -1 % 9 = 9 which is wrong
        x = int(x // 10)

        # Condition1: Prevent overflow just before adding the last digit
        # Condition2: If it passed the first condition by giving equivalent value hence checking the last digit
        if (res > MAX_VAL // 10) or (res == MAX_VAL and MAX_VAL % 10 >= digit):
            return 0
        if (res < MIN_VAL // 10) or (res == MIN_VAL and MIN_VAL % 10 <= digit):
            return 0

        res = (res * 10) + digit
    
    return res
    #  42 ms
    # if x > MIN_VAL and x < MAX_VAL:
    #     reversed_num = 0
    #     minus_flag = False
    #     if x < 0:
    #         x = abs(x)
    #         minus_flag = True
    #     while x > 0:
    #         reversed_num += (x%10) 
    #         x = x // 10
    #         if x > 0:
    #             reversed_num *= 10 
    #     if minus_flag and (0 - reversed_num) > MIN_VAL:
    #         return 0 - reversed_num
    #     elif minus_flag == False and reversed_num < MAX_VAL:
    #         return reversed_num
    # return 0

# ------------------------------------ Testing
print(reverse_integer(123456))