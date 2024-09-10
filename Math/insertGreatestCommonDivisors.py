# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            factors_of_a = [i+1 for i in range(a) if a % (i+1) == 0] 
            factors_of_b = [j+1 for j in range(b) if b % (j+1) == 0] 
            common_factors = [fact_a for fact_a in factors_of_a if fact_a in factors_of_b]
            return max(common_factors)
        cur = head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next
            prev.next = ListNode(gcd(prev.val, cur.val), cur)
        return head