from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        odd_ptr = cur_ptr = head
        even_ptr = even_head = head.next
        i = 1

        while cur_ptr:
            if i > 2 and i % 2 != 0:
                odd_ptr.next = cur_ptr
                odd_ptr = odd_ptr.next
            elif i > 2 and i % 2 == 0:
                even_ptr.next = cur_ptr
                even_ptr = even_ptr.next
            cur_ptr = cur_ptr.next
            i += 1
        even_ptr.next = None
        odd_ptr.next = even_head
        return head