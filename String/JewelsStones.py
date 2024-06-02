'''
https://leetcode.com/problems/jewels-and-stones/
'''
def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelsSet = set(jewels)
    return sum(stone in jewelsSet for stone in stones)