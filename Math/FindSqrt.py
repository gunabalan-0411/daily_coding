'''
https://leetcode.com/problems/powx-n/
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # -- Simple Solution
        # return x ** n
        # -- Iterative Solution but poor at time complexity
        # if n == 0:
        #     return 1.0
        # pow = x
        # range_val = abs(n)
        # for _ in range(1, range_val):
        #     pow *= x

        # if n < 0:
        #     return 1/pow
        # return pow

        # Efficient recursive solution
        def sqr(x, n):
            if x == 0 : return 0
            if n == 0 : return 1

            res = sqr(x, n // 2)
            res = res * res
            return x * res if n % 2 else res

        res = sqr(x, abs(n))
        return res if n >= 0 else 1/res