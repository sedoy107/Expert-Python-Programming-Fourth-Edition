"""Cython module that provides fibonacci sequence function."""
from cpython cimport array
import array

# Use memoization and do not use recursion
cdef long long fibonacci_cc(unsigned int n):
    if n < 2:
        return n

    cdef unsigned int[2] memo = [0, 1]
    for i in range(2, n + 1):
        memo[i % 2] = memo[0] + memo[1]

    return memo[n % 2]

# Original implementation
# cdef long long fibonacci_cc(unsigned int n): 
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacci_cc(n - 1) + fibonacci_cc(n - 2)

def fibonacci(unsigned int n):
    """ Return nth Fibonacci sequence number computed recursively
    """
    # The book brings up this example but it does not work
    #with nogil:
    #    result = fibonacci_cc(n)

    return fibonacci_cc(n)
