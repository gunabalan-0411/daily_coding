def jump(nums):
    res = 0
    l = r = 0
    # Using sliding window algorithm
    while r < (len(nums)-1):
        farthest = 0
        # Loop to find the farthest for r
        for i in range(l, r+1):
            farthest = max(farthest, i+nums[i])
        l = r + 1
        r = farthest
        # after each farthest we count the step
        # Basically the number for windows formed
        res += 1
    return res