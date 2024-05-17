'''
	You are given a string, s, and a list of words, words, that are all of the same length. 
    Find all starting indices of substring(s) in s that is a concatenation of each word in words 
    exactly once and without any intervening characters.

	Example 1:

	Input:
	  s = "barfoothefoobarman",
	  words = ["foo","bar"]
	Output: [0,9]
	Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
	The output order does not matter, returning [9,0] is fine too.
	Example 2:

	Input:
	  s = "wordgoodstudentgoodword",
	  words = ["word","student"]
	Output: []
'''
def findSubstring(s, words):
    # Return [] if empty inputs
    if not s or not words:
        return []

    # Creating a hash map to compare if all the words combinations are present
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    # Getting the size of string, total words, fixed word size
    n, lenWords, FixSize = len(s), len(words), len(words[0])

    # Reducing the single instance of combination size from total
    # because after that we will going to find the pattern
    result = []
    # Objective of index is if any word of size not equals fixed word
    # increment index until we find the matching word of fixed size
    for index in range(0, n - lenWords*FixSize + 1):
        # Hash map to count the seen words and compare with counts hash map
        # if counts doesn't match it fails the rule
        seen = {}
        index_j = 0
        # Iterate loop exactly the num of words as all words should present consecutively
        while index_j < lenWords:
            # index is to move the fixed word forward
            # For Ex: fixsize 3 : 6 and goes on
            word = s[index + (index_j * FixSize): index + ((index_j+1) * FixSize)]
            if word in counts:
                if word in seen:
                    seen[word] += 1
                else:
                    seen[word] = 1
                if seen[word] > counts[word]:
                    # even if a single word has seen more than actual size break
                    break
            else:
                # breaking because its not a word we should be focusing on anymore
                break
            index_j += 1
        # without breaking and passed exactly num of words in any order
        if index_j == lenWords:
            result.append(index)
    return result

print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))

        