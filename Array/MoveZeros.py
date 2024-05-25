def moveZeroes(nums) -> None:
    zeroIndex = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[zeroIndex] = nums[index]
            zeroIndex += 1
            
    for index in range(zeroIndex, len(nums)):
        nums[index] = 0