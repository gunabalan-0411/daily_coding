# Queue
class Queue(object):
    def __init__(self) -> None:
        self.items = []
    def enqueue(self, value):
        self.items.insert(0, value)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def is_empty(self):
        return len(self.items) == 0
    def __len__(self):
        return len(self.items)
        
# Stack
class Stack(object):
    def __init__(self) -> None:
        self.items = []
    def push(self, value):
        self.items.append(value)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def __len__(self):
        return len(self.items)



# Struct
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)
# Print Binary Tree
    def print_btree(self, type):
        traverse = ''
        if type == "pre-order":
            traverse = self.preorder(self.root, '')
        elif type == "in-order":
            traverse = self.inorder(self.root, '')
        elif type == "post-order":
            traverse = self.postorder(self.root, '')
        elif type == "level-order":
            traverse = self.level_order(self.root)
        elif type == "reverse-level-order":
            traverse = self.reverse_level_order(self.root)
        return traverse
    
    def preorder(self, start, traverse):
        if start:
            traverse += str(start.value) + ' -> '
            traverse = self.preorder(start.left, traverse)
            traverse = self.preorder(start.right, traverse)
        return traverse
    
    def inorder(self, start, traverse):
        if start:
            traverse = self.inorder(start.left, traverse)
            traverse += str(start.value) + ' -> '
            traverse = self.inorder(start.right, traverse)
        return traverse
    
    def postorder(self, start, traverse):
        if start:
            traverse = self.postorder(start.left, traverse)
            traverse = self.postorder(start.right, traverse)
            traverse += str(start.value) + ' -> '
        return traverse
    
# - levelorder_print
    def level_order(self, start):
        if not start:
            return
        traverse = ''
        queue = Queue()
        queue.enqueue(start)
        while len(queue) > 0:
            traverse += str(queue.peek()) + "->"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traverse
# - reverse_levelorder_print
    def reverse_level_order(self, start):
        if not start:
            return
        traverse = ''
        stack = Stack()
        queue = Queue()
        queue.enqueue(start)
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
            
        while len(stack) > 0:
            node = stack.pop()
            traverse += str(node.value) + ' -> '
        return traverse

# - height_of_tree
    def height_of_tree(self, node):
        if not node:
            return -1
        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)

        return 1 + max(left_height, right_height)
# - size_of_tree_rec
    def size_of_tree_rec(self, node):
        if not node:
            return 0
        return 1 + self.size_of_tree_rec(node.left) + self.size_of_tree_rec(node.right)

# - size of tree iterative
    def size_of_tree_iter(self, root):
        if root == None: 
            return 0
        q = [] 
        q.append(root) 
        count = 1
        while(len(q) != 0): 
            root = q.pop(0) 
            if(root.left): 
                q.append(root.left) 
                count += 1
            if(root.right): 
                q.append(root.right) 
                count += 1
        return count 
# - insert
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            return self.insert_(data, self.root)
    def insert_(self, data, cur_node):
        if data < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                # Since we don't have anything to return, we call without return
                self.insert_(data, cur_node.left)
        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self.insert_(data, cur_node.right)
        else:
            print("Data already present")
# - find
    def find(self, data):
        if self.root:
            isfound = self.find_(data, self.root)
            if isfound:
                return True
            else:
                return False
        else:
            return None
            
    
    def find_(self, data, cur_node):
        if data < cur_node.value and cur_node.left:
            return self.find_(data, cur_node.left)
        elif data > cur_node.value and cur_node.right:
            return self.find_(data, cur_node.right)
        if data == cur_node.value:
            return True



    
Tree = BinaryTree(1)
Tree.root.left = Node(2)
Tree.root.right = Node(3)
Tree.root.left.right = Node(5)
Tree.root.right.left= Node(6)
Tree.root.right.right=Node(7)
print("Pre order")
print(Tree.print_btree("pre-order"))
print("IN order")
print(Tree.print_btree("in-order"))
print("Post order")
print(Tree.print_btree("post-order"))

print("Level order")
print(Tree.print_btree("level-order"))
print("reverse_levelorder")
print(Tree.print_btree("reverse-level-order"))
print("Height of the tree : ",Tree.height_of_tree(Tree.root))
print("Size of the tree using recursive : ",Tree.size_of_tree_rec(Tree.root))

print("Level order")
print(Tree.print_btree("level-order"))
print("Size of the tree using iterative : ",Tree.size_of_tree_iter(Tree.root))
print("Going to insert ")
BTree = BinaryTree(8)
BTree.insert(3)
BTree.insert(10)
BTree.insert(1)
BTree.insert(6)
BTree.insert(9)
BTree.insert(11)
print("Level order")
print(BTree.print_btree("level-order"))
print("finding 6")
print(BTree.find(6))