from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * (len(words)+1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prev = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prev += 1
            prefix_sum[i+1] += prev
        res = []
        for q in queries:
            l, r = q[0], q[1]
            res.append(prefix_sum[r+1]-prefix_sum[l])
        return res
