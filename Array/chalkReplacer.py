from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_sum = sum(chalk)
        rem = k % total_sum
        # print(k)
        if rem == 0:
            return 0
        else:
            for i in range(len(chalk)):
                rem -= chalk[i]
                if rem < 0:
                    return i
        return 0
            