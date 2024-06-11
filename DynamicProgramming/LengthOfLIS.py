def length_of_lis(nums):
    LIS = [1] * len(nums)
    # Calculating LIS for every element from last where we could calculate from single possibility
    for i in range(len(nums)-1, -1, -1):
        # Starting index from i + 1 
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                # LIS will always be the One + next index's LIS
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)