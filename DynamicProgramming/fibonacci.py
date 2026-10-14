"""
    Write a function fib that takes in a number argument, n, and 
    returns the n-th number of the Fibonacci sequence.

    The 0-th number of the sequence is 0.
    The 1-st number of the sequence is 1.

    To generate further numbers of the sequence, calculate the sum of previous two numbers.
    Solve this recursively.

"""
 
def fib(n):
    return fib_helper(n, {})

def fib_helper(n, memo):
    if n in memo:
        return memo[n]

    
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_helper(n - 1) + fib_helper(n - 2)
    return memo[n]