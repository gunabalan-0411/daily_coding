# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pseudo_head = ListNode(0, head)

        left_node, cur = pseudo_head, head
        for i in range(left - 1):
            left_node, cur = cur, cur.next

        prev = None
        for i in range(right - left + 1):
            tmp_nxt = cur.next
            cur.next = prev
            prev = cur
            cur = tmp_nxt
        
        left_node.next.next = cur
        left_node.next = prev

        return pseudo_head.next