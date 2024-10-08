# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        while cur:
            if cur.val in nums:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next