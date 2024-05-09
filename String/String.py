'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
    "pwke" is a subsequence and not a substring.
'''
def lengthOfLongestSubstring(s: str) -> int:
        map_dict = {}
        start, result = 0, 0
        for end in range(len(s)):
            # Changing the start pointer whenever a duplicate value found
            # If previous start point is > than current start point then select the max one
            if s[end] in map_dict:
                start = max(map_dict[s[end]], start)
            # Comparing result to get the max value
            # End - Start is to get the length of any substring
            # Adding One for fixing list starts from 0
            # Get max of count
            result = max(result, end - start + 1)
            map_dict[s[end]] = end + 1
        return result

'''
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display 
    this pattern in a fixed font for better legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R

	And then read line by line: "PAHNAPLSIIGYIR"
'''

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    res_matrix = ["" for _ in range(numRows)]
    count = 0
    down = True
    up = False
    for i in range(len(s)):
        res_matrix[count] += s[i]
        if down and count < numRows-1:
            count += 1
        elif up:
            count -= 1
        
        if count == numRows - 1:
            down = False
            up = True
        elif count == 0:
            down = True
            up = False
    return "".join([res for res in res_matrix])


'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

https://leetcode.com/problems/longest-common-prefix/description/
'''

def longestCommonPrefix(strs):
    # 44 ms
    prefix_so_far = True
    len_of_strs = len(strs)
    min_str = min(strs, key = len)
    min_str_len = len(min_str)
    prefix_pointer = 0
    res = ''
    if len_of_strs == 1 or min_str_len == 0:
        return min_str
    while prefix_so_far and prefix_pointer < min_str_len:
        ch = min_str[prefix_pointer]
        for i in range(len_of_strs):
            if prefix_pointer < min_str_len and strs[i][prefix_pointer] != ch:
                prefix_so_far = False
        if prefix_so_far:
            res += ch
            prefix_pointer += 1
    return res
# 35 ms
def longestCommonPrefix(strs):
    def prefix(strs, index):
        check_prefix = strs[0][:index]
        for i in range(1, len(strs)):
            if not strs[i].startswith(check_prefix):
                return False
        return True
    
    if not strs:
        return ""
    
    min_size = float('inf')
    for i in range(len(strs)):
        min_size = min(min_size, len(strs[0]))

    low, high = 0, min_size

    while low <= high:
        mid = int((low+high)/ 2)
        if prefix(strs, mid):
            low = mid + 1
        else:
            high = mid - 1

    return strs[0][: int((low+high)/2)]


# -------------------------------------------------------------Testing----------------------------------------------
print(lengthOfLongestSubstring("pwwkew"))
print("Zigzag Convertion", convert("PAYPALISHIRING", 3))