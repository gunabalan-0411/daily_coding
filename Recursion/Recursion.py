# Aim is to reduce the input step by step
# If its involve a Choices + Decision is a Recursion Problem
# Ex: Get subset of "abc"
#   -> we have 2 choices whether to consider or not for a subset
#   -> So, on these choices whatever decision I will take, it will make my subset!
# Recursion is backbone of :- Dynamic programming / BackTracking / Divide n Conquer


# Hypothesis-Induction-Base Condition
def print_n_(n):
    # Base
    if n == 0:
        return
    print(n, end = '->')
    print_n_(n-1)

# ------------------------------------------------------------ Execution------------------------------------------------------------
print_n_(7)



