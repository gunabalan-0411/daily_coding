'''
	Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

	A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
def letterCombinations(digits):
    num_pad = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' 
        }
    if digits == "":
        return []
    
    # Starting with empty string as we should start with empty string and first digit pairing
    result = ['']

    # Don't try to combine all 3 elements at once, go by 1, 2, 3 and so on 
    # then combine whatever values with latest combinations

    for char in digits:
        values = num_pad[char]
        new_result = []
        for prefix in result:
            # current element it will be single element for first iteration, 2 elementes for 2nd & so on
            currElement = prefix
            for value in values:
                # combining previous combinations with remaing values from digits
                new_result.append(currElement + value)
        # overwrite the combinations
        result = new_result

    return result

print(letterCombinations('23'))