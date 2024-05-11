'''
	Given a linked list, remove the n-th node from the end of list and return its head.

	Example:

	Given linked list: 1->2->3->4->5, and n = 2.

	After removing the second node from the end, the linked list becomes 1->2->3->5.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        cur_node = head
        i = 0
        l_len = 0
        temp = head
        # Calculate the length of linked list
        while temp:
            l_len += 1
            temp = temp.next
        
        prev_node = None
        while cur_node:
            # Case 1: if node to be delete is head node
            # Directly change the head node and return it
            if l_len - n == 0:
                head = cur_node.next
                return head
            # Case 2: if any other node
            # Just change the duplicate object and return the original
            if i == l_len - n:
                prev_node.next = cur_node.next
                cur_node.next = None
                return head
            prev_node = cur_node
            cur_node = cur_node.next
            i += 1