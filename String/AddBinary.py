'''
https://leetcode.com/problems/add-binary/description/
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        car = 0
        while a != '' or b != '':
            n1 = n2 = 0
            if a != '':
                n1 = int(a[-1])
                a = a[:-1]
            if b != '':
                n2 = int(b[-1])
                b = b[:-1]
            sum = n1 + n2 + car

            if sum == 2 or sum == 0:
                res = '0' + res
            else:
                res = '1' + res
            car = 1 if sum > 1 else 0
        return '1'+res if car==1 else res
