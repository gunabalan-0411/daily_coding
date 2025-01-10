from typing import List
from collections import defaultdict, Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)
        for w in words2:
            count_w = Counter(w)
            for w, cnt in count_w.items():
                count_2[w] = max(count_2[w], cnt)
        count_1 = defaultdict(int)
        res = []
        for word in words1:
            count_w = Counter(word)
            flag = True
            for w, cnt in count_2.items():
                if count_w[w] < cnt:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res
                