# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur_node = head
        trace_node = ListNode(0)
        res_node = trace_node
        prev_node = None
        while cur_node.next:
            if cur_node.val != cur_node.next.val:
                trace_node.next = ListNode(cur_node.val)
                prev_node = trace_node
                trace_node = trace_node.next
                cur_node = cur_node.next
            else:
                while cur_node.next and cur_node.val == cur_node.next.val:
                    cur_node = cur_node.next
                if cur_node.next:
                    cur_node = cur_node.next
                else:
                    return res_node.next
        if cur_node.val == trace_node.val:
            prev_node.next = None
        else:
            trace_node.next = ListNode(cur_node.val)
        return res_node.next
        