'''
    https://leetcode.com/problems/merge-k-sorted-lists/submissions/1256289559/
	Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

	Example:

	Input:
	[
	  1->4->5,
	  1->3->4,
	  2->6
	]
	Output: 1->1->2->3->4->4->5->6

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(lists):
    # Algorithm to merge two linked lists
    # Will use a pointer to attach next smallest node
    def merge2llists(l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = ListNode(l1.val)
                l1 = l1.next
            else:
                point.next = ListNode(l2.val)
                l2 = l2.next

            point = point.next
        # After either one of the linkedlist is ran out, need to attach 
        # the remained sorted list to so far sorted pointer
        if l1:
            point.next = l1
        else:
            point.next = l2

        return head.next

    if not lists:
        return None
    
    size = len(lists)
    interval = 1
    # iterate over the linked lists and always store result at 0th position
    # and merge the result at 0th position and other lists
    while interval < size:
        for index in range(0, size - interval, interval * 2):
            lists[index] = merge2llists(lists[index], lists[index + interval])
        interval *= 2

    return lists[0]
    