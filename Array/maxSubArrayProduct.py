def maxProduct(nums):
    # all positive, product always increment
    # if all negative, different signs for consecutive numbers product
    # have to maintain maxprod & minprod
    # -- [-1,     |-2|,    -3] = [-2 . -3] = 6
    #            2     -2
    #        maxprod, minprod
    # so every time we get maxprod by max of n * maxprod or n * minprod or n itself
    # in next step calculate minprod as well

    # another edge case is 0
    # anything product 0 is 0 hence will set min, max to neutral which is 1 for product of next num
    maxSum = max(nums)
    maxProd, minProd = 1, 1
    for n in nums:
        if n == 0:
            maxProd, minProd = 1, 1
            continue

        tmp = n * maxProd
        maxProd = max( n * maxProd, n * minProd, n)
        minProd = min(tmp, n * minProd, n)
        maxSum = max(maxSum, maxProd)

    return maxSum
