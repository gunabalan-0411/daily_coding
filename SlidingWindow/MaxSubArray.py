def maxSubArray(nums):
    maxSub = nums[0]
    curSub = 0

    for num in nums:
        # Since we have to find the largest sum
        # Adding negatives makes it smaller
        if curSub < 0:
            curSub = 0
        curSub += num

        maxSub = max(maxSub, curSub)

    return maxSub

print(maxSubArray([-2, -4, -1, -9]))