#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer.

    Parameters:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Command-line argument is the input number for factorial calculation
f = factorial(int(sys.argv[1]))
print(f)
