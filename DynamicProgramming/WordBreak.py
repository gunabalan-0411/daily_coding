'''
https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
def wordBreak(s, wordDict):
    s_len = len(s)
    # Initialize Dynamic Programming Cache
    # To include '' Empty String + 1
    dp_cache = [False for _ in range(s_len + 1)]
    dp_cache[0] = True

    # Iterating each and every char in string
    for idx_i in range(s_len):
        # Iterate to get a substring that not seen so far
        for idx_j in range(idx_i, -1, -1):
            sub_string = s[idx_j: idx_i + 1] # +1 for not inclusive

            # Using dp_cache to check if string so far is passed
            # And check if substring after the captured substring is found
            if dp_cache[idx_j] and sub_string in wordDict:
                # +1, Since we add extra one space of empty 
                dp_cache[idx_i + 1] = True
                break

    return dp_cache[s_len]