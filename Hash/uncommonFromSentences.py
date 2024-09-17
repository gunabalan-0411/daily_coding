from typing import List, Optional

"""
884. Uncommon Words from Two Sentences

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.


Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
"""
import collections
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # count = collections.Counter((s1 + ' ' + s2).split())
        # return [word for word, freq in count.items() if freq == 1]
        word_maps = {}
        for word in s1.split(' '):
            if word not in word_maps:
                word_maps[word] = 0
            word_maps[word] += 1
        for word in s2.split(' '):
            if word not in word_maps:
                word_maps[word] = 0
            word_maps[word] += 1
        res = []
        for word, count in word_maps.items():
            if count == 1:
                res.append(word)
        return res
s1 = "fd kss fd"
s2 = "fd fd kss"
print(Solution().uncommonFromSentences(s1, s2))