# - Struct
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
# - Append
    def append(self, data):
        if not self.head:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = None
            new_node.prev = cur_node
# - Prepend
    def prepend(self, data):
        if not self.head:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.prev = None
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

# - Print Llist
    def print_dlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end = '->')
            cur_node = cur_node.next
        print()

# - Add Before node
    def add_before_node(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.prev == None and cur_node.data == key:
                self.prepend(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                tmp = cur_node.prev
                cur_node.prev = new_node
                new_node.next = cur_node
                new_node.prev = tmp
                tmp.next = new_node
            cur_node = cur_node.next

# - Add After node
    def add_after_node(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.next == None and cur_node.data == key:
                self.append(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                nxt = cur_node.next
                cur_node.next = new_node
                new_node.prev = cur_node
                new_node.next = nxt
                nxt.prev = new_node
            cur_node = cur_node.next

# - Delete
    def delete(self, key):
        cur_node = self.head
        while cur_node:
            if cur_node == self.head and cur_node.data == key:
				# Case 1: only one node which is head
                if cur_node.next == None:
                    cur_node = None
                    self.head = None
                    return
				# Case 2: only two node and to get deleted is 1st head node
                else:
                    nxt = cur_node.next
                    cur_node.next = None
                    cur_node = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif cur_node.data == key:
				# Case 3: node to be deleted is present in between any two node
                if cur_node.next:
                    prev = cur_node.prev
                    nxt = cur_node.next
                    prev.next = nxt
                    nxt.prev = prev
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
				# Case 4: node to be deleted is the end node
                else:
                    prev = cur_node.prev
                    prev.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
            cur_node = cur_node.next

# - Reverse
    def reverse(self):
        tmp = None
        cur = self.head
        # Think about swaping one pair and rest will follow the same pattern
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        # After loops ends the pointer will be point to the last node (now moved to 1st node)
        # hence setting it as head node
        if tmp:
            self.head = tmp.prev

# - remove duplicates
    def remove_duplicates(self):
        cur = self.head
        unique_list = []
        while cur:
            if cur.data not in unique_list:
                unique_list.append(cur.data)
            else:
                self.delete(cur.data)
            cur = cur.next

# - pairs with sum
    def pairs_with_sum(self, sum_val):
        tmp = self.head
        cur = self.head
        ddlist = []
        result = []
        while tmp:
            ddlist.append(tmp.data)
            tmp = tmp.next
        
        while cur:
            if sum_val - cur.data in ddlist:
                if (str(cur.data) + " " + str(sum_val-cur.data))[::-1] not in result:
                    result.append(str(cur.data)+ " " + str(sum_val-cur.data))
                    print(str(cur.data)+ " " + str(sum_val-cur.data))
            cur = cur.next
            

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
print("Append 1, 2")
dllist.print_dlist()
print("Prepend 0")
dllist.prepend(0)
dllist.print_dlist()
print("After Node", 2, 4)
dllist.add_after_node(2,4)
dllist.print_dlist()
print("Before Node", 4, 3)
dllist.add_before_node(4,3)
dllist.print_dlist()
print("Deleting 0")
dllist.delete(0)
dllist.print_dlist()
print("Reversing")
dllist.print_dlist()
dllist.reverse()
dllist.print_dlist()
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
print("Removing Duplicates")
dllist.print_dlist()
dllist.remove_duplicates()
dllist.print_dlist()
print("sum values of 5")
dllist.pairs_with_sum(5)
print("double list")
dllist.print_dlist()