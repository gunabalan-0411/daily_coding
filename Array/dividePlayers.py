from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        size = len(skill)
        products = []
        equality_check = []
        for i in range(len(skill)//2):
            products.append(skill[i] * skill[size-1-i])
            equality_check.append(skill[i] + skill[size -1 -i])
        if len(set(equality_check)) != 1:
            return -1
        return sum(products)

        