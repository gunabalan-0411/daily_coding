'''
https://leetcode.com/problems/unique-binary-search-trees/description/
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n 
nodes of unique values from 1 to n.
'''
def numTrees(n):
    # To calculate number of unique structure for n = 4
    # 1. Take each node from possible nodes 1 to 4 as root [1, 2, 3, 4]
    # -- The first level of tree formation requires
    # Ex: numTree[4] - with 1 as root = numTree[0] * numTree[3] +
    #                  with 2 as root   numTree[1] * numTree[2] +
    #                  with 3 as root   numTree[2] * numTree[1] +
    #                  with 4 as root   numTree[3] * numTree[0]

    # The reason we are multiplying the num of trees in left and right is for to get total combinations 
    # we have to multiply
    # With dynamic programming we will calculate the sub level counts before we come to actual n 

    # We consider null when all the nodes move to right side
    numTree = [1] * (n+1)

    # Num of Tree for 0 and 1 is 1, these two values help to calculate for 2 and so on
    for nodes in range(2, n+1):
        total = 0
        for root in range(1, nodes+1):
            # Check the example from comments
            left = root - 1
            right = nodes - root
            total += numTree[left] * numTree[right]
        numTree[nodes] = total

    return numTree[n]