from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        ROW, COL = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, word, node):
            # base case
            if (
                r < 0 or c < 0 or
                r == ROW or c == COL or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r-1, c, word, node)
            dfs(r+1, c, word, node)
            dfs(r, c-1, word, node)
            dfs(r, c+1, word, node)
            visit.remove((r, c))
        
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, '', root)
        return list(res)