# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_k_group(head, k):
    dummy = ListNode(0, next = head)
    groupPrev = dummy
    while True:
        # Function to get the kth element in every group i.e the last element in every group
        kth = KthNode(dummy, k)

        # Handling the special condition by not reversing the nodes which overall size is < k
        if not kth:
            break
        # We will use this to iterate the current subgroup until the next subgroup
        groupNext = kth.next

        # If we set prev = Null like we do usually, it will break the linkedlist
        # Hence setting th prev node be the first node of next sub group
        prev, cur = kth.next, groupPrev.next
        while cur != groupNext:
            tmp = cur.next
            cur.next = prev
            prev = cur
            # Forward iterating irrespective change in diection
            cur = tmp

        tmp = groupPrev.next
        # Connecting the group prev to kth because now kth is the first element of the sub group 
        groupPrev.next = kth
        # Setting actual group prev which should be the last element of the sub group (which is the first one previously)
        groupPrev = tmp


def KthNode(cur, k):
    while cur and k > 0:
        cur = cur.next
        k -= 1
    return cur
