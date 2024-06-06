def countBits(n):
    # 86 ms: my solution
    # def count_bits(num):
    #     count = 0
    #     while num > 0:
    #         num &= (num - 1)
    #         count += 1
    #     return count

    # res = []
    # for i in range(n+1):
    #     res.append(count_bits(i))
    # return res
    # -- 60 ms
    # dynamic programming cache to store results
    dp = [0] * (n + 1)
    # highest power of 2
    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        # for every (power of 2) bits extra one is added in binary representation            
        dp[i] = 1 + dp[i-offset]
    return dp
