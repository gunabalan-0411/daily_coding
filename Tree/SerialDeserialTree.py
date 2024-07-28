# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.tree = None

    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        self.i = 0
        arr = data.split(',')
        def dfs():
            if arr[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(str(arr[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

        