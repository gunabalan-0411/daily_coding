def combinationSum2(candidates, target):
    # we will sorting the array first, to avoid usage of same combinations like 1, 7 and 7, 1
    # it will be always going to be 1, 7 and when sorted we skip the same number for the elements of
    # next sub tree
    #                   [1, 1, 2, 6, 7, 10]
    #                   1                []
    #               1      7         2        []
    #           2     []   Y      6   []   6     []  
    #         6         6         Y      7   []
    #         X          Y               X    X
    # 3 Solutions in above (Y)
    candidates.sort()
    res = []
    def backtracking(cur, pos, target):
        if target == 0:
            res.append(cur.copy())
            return

        if target <= 0:
            return

        prev = -1
        for i in range(pos, len(candidates)):
            # Skiping if same number
            if candidates[i] == prev:
                continue

            cur.append(candidates[i])
            
            backtracking(cur, i+1, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtracking([], 0, target)
    return res
