'''
	Given a linked list, swap every two adjacent nodes and return its head.

	Example:

	Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if not head:
        return None
    
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head