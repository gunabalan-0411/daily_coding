class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [
            indx for indx, word  in enumerate(words) if x in word
        ]