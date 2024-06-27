'''
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list_of_all_ch = [ord(ch) for ch in sentence]
        unique = len(set(list_of_all_ch))
        return unique==26
        