def climbStairs(n):
    # Edge Case
    if n == 0:
        return 0
    
    # Initialize Dynamic Programming
    dp_cache = [0] * n

    # Initialize for both 1st and 2nd
    dp_cache[0] = 1

    if n > 1:
        dp_cache[1] = 2

        # Since already filled for 1 and 2
        for index in range(2, n):
            # Permutation formula
            dp_cache[index] = dp_cache[index - 1] + dp_cache[index - 2]

    return dp_cache[n-1]