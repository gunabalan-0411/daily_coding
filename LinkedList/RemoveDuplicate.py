# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        trace_node = ListNode(0)
        res = trace_node
        unique = []
        while cur_node:
            if cur_node.val not in unique:
                unique.append(cur_node.val)
                trace_node.next = ListNode(cur_node.val)
                trace_node = trace_node.next
            cur_node = cur_node.next
        return res.next
        