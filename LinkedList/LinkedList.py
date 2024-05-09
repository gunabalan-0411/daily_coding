
# Struct
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

# Append
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node            
# Prepend
    def prepend(self, data):
         new_node = Node(data)
         if self.head is None:
              self.head = new_node
              return
         new_node.next = self.head
         self.head = new_node
# print_llist
    def print_llist(self):
         cur_node = self.head
         while cur_node:
              print(cur_node.data,'-> ', end = "")
              cur_node = cur_node.next
         print("")
# -- DAY 2
# Search -> return Node
    def search_llist(self, search_data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == search_data:
                return cur_node
            cur_node = cur_node.next

# Insert after Node
    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
# Delete Node By Value
    def delete_node_by_value(self, key):
        cur_node = self.head
        # If the data is head node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        # Delete the data after any node
        prev = None

        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node.next = None

# Length
    def length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

# Swap
    def swap_nodes(self, a_node, b_node):
        a_node.data, b_node.data = b_node.data, a_node.data

# Delete node by position
    def delete_node_by_position(self, index):
        i = 0
        cur_node = self.head
        prev_node = None
        if index == 0:
            self.head = cur_node.next
            cur_node = None
            return
        while cur_node:
            if i == index:
                prev_node.next = cur_node.next
                cur_node.next = None            
            i = i+1
            prev_node = cur_node
            cur_node = cur_node.next

# Reverse
    def reverse(self):
        prev_node = None
        cur_node = self.head
        while cur_node:
            # Indirect increment to not lose forward direction while assigning
            # cur_node.next = prev
            next = cur_node.next
            # This makes the actual reverse
            cur_node.next = prev_node
            # Storing the previous Node like any other operations
            prev_node = cur_node
            # Incrementing forward direction
            cur_node = next
        # finally assigning the head node to final prev node
        self.head = prev_node

# Merge Sorted
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        #check if any llist missing , if so then return the only one llist
        if p is None:
            return q
        if q is None:
            return p
        #initialize the three pointers position
        if p and q:
            if p.data < q.data:
                s = p
                p = p.next
            else:
                s = q
                q = q.next
            new_head = s
        # looping stage
        while p and q:
            if p.data < q.data:
                #attaching s
                s.next = p
                #move s , so that u can link the next small item to s
                s= s.next
                p = p.next
            else:
                s.next = q
                s = s.next
                q = q.next
        # after looping either one of the two pointers p or q will be
        # None 
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

# Remove duplicate
    def remove_duplicate(self):
        cur_node = self.head
        prev_node = None
        unique_list = []
        while cur_node:
            if cur_node.data not in unique_list:
                unique_list.append(cur_node.data)
                # Reason inside this condition is, we don't need the deleted alone 
                # node as the previous node.
                prev_node = cur_node
            else:
                prev_node.next = cur_node.next
                cur_node = None
            
            cur_node = prev_node.next

# Print Nth from last
    def print_nth_from_last(self, n):
        cur_node = self.head
        i = 0
        while cur_node:
            if i >= n:
                print(cur_node.data)
            cur_node = cur_node.next
            i += 1

# Occurence
    def occurence(self, val):
        cur_node = self.head
        count = 0
        while cur_node:
            if cur_node.data == val:
                count += 1
            cur_node = cur_node.next
        return count

# Rotate
    def rotate(self, k):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

# Is Palindrome - String Method
    def is_palindrome_by_str(self):
        s = ''
        cur_node = self.head
        while cur_node:
            s += cur_node.data
            cur_node = cur_node.next
        
        return s == s[::-1]

# Is Palindrome - list reverse check Method
    def is_palindrome_by_list_reverse(self):
        p = self.head
        q = self.head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        
        count = 1
        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True


# Move Tail to Head
    def move_tail_to_head(self):
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

# Sum of two lists
    def sum_two_llist(self, sec):
        # Leetcode solution: https://leetcode.com/problems/add-two-numbers/
        p = self.head
        q = sec.head
        sum_llist = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_llist() 

    




llist = LinkedList()
llist.append('b')
llist.append('c')
llist.prepend('a')
llist.print_llist()
print("Done Append, Prepend, Print Llist Testing")

print("\nSearching b node")
print(llist.search_llist('b'))
print("\nInserting d after b node")
llist.insert_after_node(llist.search_llist('b'), 'd')
llist.print_llist()
print('\nDeleting node d')
llist.delete_node_by_value('d')
llist.print_llist()
print('\nCalculating Length')
print(llist.length())
print('\nSwapping c and a nodes')
llist.swap_nodes(llist.search_llist('c'), llist.search_llist('a'))
llist.print_llist()
print("\nDone Search Node, Insert After Node, Delete Node by Value, Length, Swap Nodes")
print("Delete Node by Position")
llist.print_llist()
llist.delete_node_by_position(llist.length()-1)
llist.print_llist()
llist.append('d')
llist.prepend('a')

print("Reversing")
llist1 = LinkedList()
llist1.append("1")
llist1.append("b")
llist1.append("c")
llist1.append("d")
llist1.print_llist()

llist1.reverse()
llist1.print_llist()

print("Linked list merge two sorted linked list")
ll1=LinkedList()
ll2=LinkedList()
ll1.append(1)
ll1.append(5)
ll1.append(7)
ll1.append(9)
ll1.print_llist()
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(6)
ll2.print_llist()
ll1.merge_sorted(ll2)
ll1.print_llist()

print("removing duplicate")
duplist = LinkedList()
duplist.append("a")
duplist.append("b")
duplist.append("b")
duplist.append("c")
duplist.append("d")
duplist.append("c")
duplist.append("a")
duplist.remove_duplicate()
duplist.print_llist()
print("print nth from last")
nlist = LinkedList()
nlist.append(1)
nlist.append(2) 
nlist.append(3)
nlist.append(4)
nlist.print_nth_from_last(1)
print("Occurence of 1",nlist.occurence(1))
print("After rotate")
nlist.rotate(3)
nlist.print_llist()

print("palindrome check")
pal = LinkedList()
pal.append("r")
pal.append("a")
pal.append("d")
pal.append("a")
pal.append("r")

pal.print_llist()
print(pal.is_palindrome_by_str())
pal.move_tail_to_head()
pal.print_llist()
print(pal.is_palindrome_by_list_reverse())


print("add two linked list")
l1=LinkedList()
l2=LinkedList()
l1.append(5)
l1.append(6)
l1.append(3)
l2.append(8)
l2.append(4)
l2.append(2)
l1.print_llist()
l2.print_llist()
print(365 + 248)
l1.sum_two_llist(l2)