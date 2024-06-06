def firstMissingPositive(A):
    # Using O(3*n) but its still O(n)

    # We don't need negative numbers here, since the context range is
    # between 1 and n, hence changing the negative values with neutral value 0
    for i in range(len(A)):
        if A[i] < 0:
            A[i] = 0

    # Iterate the Array to mark in the same array whether if a number is present or not
    # by changing the number - 1 th index of the array so that we track it later
    for i in range(len(A)):
        val = abs(A[i])
        # check if the value is inbound and we don't care about out of bound values
        if 1 <= val <= len(A):
            # only if the marking area is not already marked
            if A[val - 1] > 0:
                A[val - 1] *= -1
            # if its zero then forcibly making it out of bound
            elif A[val - 1] == 0:
                A[val - 1] = -1 * (len(A)+1)
    
    # Re-tracking now, since we know what the ideal range could be
    for i in range(1, len(A) + 1):
        # if greater than zero then its not found also
        # since we start from 1 its going to be the smallest 
        if A[i-1] >= 0:
            return i
    # worst case scenario
    return len(A) + 1