def hammingWeight(n):
    # 33 ms: my solution
    # return str(bin(n))[2:].count('1')

    # 35 ms: bit wise algorithm
    # modulus of each bit by 2 gives the count
    res = 0
    # while n:
    #     res += n % 2
    #     n = n >> 1 
    # return res
    # brute force
    # count = 0
    # while n:
    #     count += n & 1 
    #     n = n >> 1
    # return count
    # 19 ms instead of iterate each bit, directly hit 1s
    while n:
        n &= (n -1)
        res += 1
    return res