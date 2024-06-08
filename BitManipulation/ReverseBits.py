def reverseBits(n):
    res = 0
    for i in range(32):
        # 1 & with the any number gives the same number
        bit = (n >> i) & 1
        # shift the captured bit
        res |= bit << (31 - i)
    return res