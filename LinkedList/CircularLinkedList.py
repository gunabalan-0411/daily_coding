# Struct
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self) -> None:
        self.head = None

# Prepend
    def prepend(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node            
        else:
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.head = new_node

# Append
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head           
            
# Print CLList
    def print_cllist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end = '->')
            cur_node = cur_node.next
            
            if cur_node == self.head:
                break
        print('')

# - remove by value
    def remove_by_val(self, key):
        if self.head.data == key:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            while cur_node.next != self.head and cur_node.data != key:
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = cur_node.next
            cur_node.next = None

# - __len__
    def __len__(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        return count
            
# - split_list
    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        
        # Part 1
        mid = size // 2
        cur = self.head
        count = 0
        prev = None
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        # Part 2
        sec_clist = CircularLinkedList()
        while cur.next != self.head:
            sec_clist.append(cur.data)
            cur = cur.next
        sec_clist.append(cur.data)

        print("first part")
        self.print_cllist()
        print("Second part")
        sec_clist.print_cllist()

# - remove node
    def remove_by_node(self, node):
        if self.head == node:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            cur_node = self.head
            while cur_node.next != self.head and cur_node != node:
                prev = cur_node
                cur_node = cur_node.next 
            prev.next = cur_node.next
            # cur_node.next = None

# - Josephus Circle
    def josephus_circle_elimination(self, step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                count += 1
                cur = cur.next
            print("REMOVED " + str(cur.data))
            self.remove_by_node(cur)
            cur = cur.next


# - Is circular linked list
    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur:
            cur = cur.next
            if cur == input_list.head:
                return True
        return False

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.prepend(3)
cllist.prepend(4)
cllist.print_cllist()

print("remove 3")
cllist.remove_by_val(3)
cllist.print_cllist()
print("remove 4")
cllist.remove_by_val(4)
cllist.print_cllist()
cllist.remove_by_node(cllist.head)
cllist.print_cllist()
cllist.append(3)
cllist.append(4)
cllist.append(5)
cllist.append(6)
print("before split")
cllist.print_cllist()
cllist.split_list()
print(cllist.is_circular_linked_list(cllist))

cllist.append(3)
cllist.append(4)
cllist.append(5)
cllist.append(6)
print("Josephus Circule Elimination")
cllist.print_cllist()
cllist.josephus_circle_elimination(3)
cllist.print_cllist()

