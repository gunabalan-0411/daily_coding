# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if k == 0:
            return head
        if not head:
            return None

        tempHead, length = head, 1
        while tempHead.next:
            length += 1
            tempHead = tempHead.next

        # Making Cicular linked list
        tempHead.next = head
        # Calculate reminder to avoid unnecessary iteration
        jump = (length - k) % length
        
        prevNode = tempHead
        while jump > 0:
            prevNode = prevNode.next
            jump -= 1

        head = prevNode.next
        prevNode.next = None

        return head