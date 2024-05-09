'''Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.'''
# https://leetcode.com/problems/integer-to-roman/description/
# 51 ms
def intToRoman(num: int) -> str:
        roman_dict = {
             1    : 'I',
             5    : 'V',
             10   : 'X',
             50   : 'L',
             100  : 'C',
             500  : 'D',
             1000 : 'M'
        }
        def get_roman(digit, tens, subtractive_form):
            full_num = digit * tens
            for index, n in enumerate(roman_dict):
                # To handle subtractive form 
                if n > full_num and subtractive_form:
                    return roman_dict[n - full_num] + roman_dict[n]
                # To handle no subtractive form (straight forward)
                if full_num // n == 1 and subtractive_form == False:
                    return roman_dict[n] + int((full_num-n) / tens) * roman_dict[tens]
            # Edge case for 1, 2, 3 and their tens
            if (full_num//tens == digit):
                return digit * roman_dict[tens]                   
        romans = []
        no_tens = 0 
        subtractive_form = False
        while num > 0:
            remainder = num % 10 
            num = num // 10

            if remainder == 9 or remainder == 4:
                subtractive_form = True
            else:
                subtractive_form = False

            romans.append(get_roman(remainder, 10 ** no_tens, subtractive_form))
            no_tens += 1
        
        return ''.join(romans[::-1])

# 44 ms
def intToRoman(num: int) -> str:
        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
            ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],
            ["D", 500], ["CM", 900], ["M", 1000]
        ]
        res = ''
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res += (count * sym)
                num = num % val

        return res