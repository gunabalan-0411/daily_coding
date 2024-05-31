'''
https://leetcode.com/problems/combination-sum/
'''
def combinationSum(candidates, target):
    # Design a Decision Tree (helps to easy grasp of concept)
    # Instead of a normal decision tree for combinations (which could lead to duplicates)
    # Write a decision tree keeping one element on left and remaining elements on right recursively
    # In that way we increment the minority until a completing element to total up the target
    result = []

    def dfs(i, cur, total):
        # Base case for success:
        if total == target:
            result.append(cur.copy())
            return 
        # Base case to avoid infinity/ out of index
        if i >= len(candidates) or total > target:
            return

        # Adding an element or multiple of same element
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        # Popping the last element before right tree branching where the current element
        # shouldn't be present to avoid duplicate
        cur.pop()
        dfs(i+1, cur, total) # same total as we popped the last element
    dfs(0, [], 0)
    return result