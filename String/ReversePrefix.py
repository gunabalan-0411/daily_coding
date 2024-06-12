class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word[0:word.find(ch)+1][::-1]+word[word.find(ch)+1:]