class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    if not head:
        return None

    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev