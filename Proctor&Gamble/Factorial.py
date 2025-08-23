# python
from GeneralConcepts import timer


def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120

# python
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(factorial(5))  # Output: 120


# python
def factorial(n, memo=None):
    if memo is None:
        memo = {}
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
    else:
        memo[n] = n * factorial(n - 1, memo)
    return memo[n]

# Example usage
print(factorial(5))  # Output: 120



# python
import math

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return math.factorial(n)

# Example usage
print(factorial(20))  # Output: 120