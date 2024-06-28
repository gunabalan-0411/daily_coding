# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        cur = head
        visitSet = set()
        while cur:
            if cur not in visitSet:
                visitSet.add(cur)
            else:
                return True
            cur = cur.next

        return False