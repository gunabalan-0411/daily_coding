# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        part1 = ListNode()
        p = part1
        part2 = ListNode()
        q = part2
        while cur:
            if cur.val >= x:
                q.next = ListNode(cur.val)
                q = q.next
            else:
                p.next = ListNode(cur.val)
                p = p.next
            cur = cur.next
        p.next = part2.next
        return part1.next


        