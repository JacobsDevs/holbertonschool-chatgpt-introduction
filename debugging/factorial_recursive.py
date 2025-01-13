#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    This function computes the factorial of a number by multiplying it 
    by the factorial of the number one less than it, recursively, until 
    it reaches 0. The factorial of 0 is defined as 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of n. If n is 0, returns 1 as 0! is defined as 1.

    Example:
    factorial(5) returns 120, because 5! = 5 * 4 * 3 * 2 * 1 = 120.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))  # Get the number from the command-line argument
print(f)  # Print the calculated factorial
