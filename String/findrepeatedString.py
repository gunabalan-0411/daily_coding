def findRepeatedDnaSequences(s):
    seen, res = set(), set()
    for i in range(len(s) - 9):
        cur = s[i: i+10]
        if cur in seen:
            res.add(cur)
        seen.add(cur)
    return res