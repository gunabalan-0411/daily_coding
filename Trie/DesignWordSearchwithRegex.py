class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.EndofWord = False
class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()
            cur_node = cur_node.children[ch]
        cur_node.EndofWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                ch = word[i]
                if ch == '.':
                    for node in cur.children.values():
                        if dfs(i+1, node):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.EndofWord
        return dfs(0, self.root)
            



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)