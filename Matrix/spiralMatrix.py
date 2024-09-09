# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left, right = 0, n
        top, bottom = 0, m
        grid = [[-1 for i in range(n)] for j in range(m)]
        r, c = 0, 0
        d = 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while head:
            dr, dc = direction[d]
            while (head and  left <= c < right and  top <= r < bottom and (grid[r][c] == -1)):
                grid[r][c] = head.val
                head = head.next
                r, c = r + dr, c + dc
            r, c = r - dr, c - dc
            d = (d+1) % 4
            dr, dc = direction[d]
            r, c = r+dr, c + dc
        return grid




        
