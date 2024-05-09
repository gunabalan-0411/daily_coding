# Struct
class Trie():
    def __init__(self) -> None:
        self.head = {}
# Add word
    def add_word(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True
# Search word
    def search_word(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' not in cur:
            return False
        return True 

trie = Trie()
trie.add_word('work')
trie.add_word('worker')
print(trie.head.items())
print('Search wor', trie.search_word('wor'))
print('Search work', trie.search_word('work'))
print('Search worker', trie.search_word('worker'))

