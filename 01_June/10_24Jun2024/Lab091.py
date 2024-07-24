# recursion

# rescursion is programming tech where a function
# calls itself in order to solve a problem

# key concept
# base case
# recursive case

# factorial
n = 5

def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n-1)

print(factorial(5))