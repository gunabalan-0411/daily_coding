import copy
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Solution 1: 
def cloneGraph(node):
    return copy.deepcopy(node)

# Solution 2: Using Depth First Search
def cloneGraph(node):
    oldtoNew = {}

    def depth_copy(node):
        # Since it is a undirected graph, to bidirection might be exist
        # In that case to avoid repeating node creation maping already created node to neighbor
        if node in oldtoNew:
            # return existing node
            return oldtoNew[node]
        
        # Make a copy by value
        copy = Node(node.val)
        # Add it to the cache
        # register the new one as value for the old one as key
        oldtoNew[node] = copy

        # Also copy of that neighbors and add to the cloned node's neighbors
        # recursively navigate to the neighbors and return the existing node or new node
        for nei in node.neighbours:
            copy.neighbours.append(
                depth_copy(
                    nei
                ))
        # return newly created node
        return copy
    
    return depth_copy(node) if node else None