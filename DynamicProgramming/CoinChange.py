def coinChange(coins, amount):
    # Setting each value to be a higher than amount to track if coins possible later
    # since we calculate 0 to amount its * (amount + 1)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    # 0 just calculated
    for a in range(1, amount + 1):
        for c in coins:
            # minimum of so far and current coin count(1) + dp(cache) of remaining coins
            if (a - c) >= 0:
                dp[a] = min(dp[a], 1 + dp[a-c])
    # edge case
    return dp[amount] if dp[amount] != (amount + 1) else -1