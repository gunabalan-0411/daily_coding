def plusOne(digits):
    for i, d in reversed(list(enumerate(digits))):
        if d < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

print(plusOne([2,2,9,9]))