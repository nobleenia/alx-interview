#!/usr/bin/python3
"""
This module contains a function that calculates
the minimum number of operations needed
to reach exactly n 'H' characters in a text file
using only Copy All and Paste operations.
"""


def minOperations(n):
    """
    Determine the minimum number of operations
    needed to result in exactly n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required,
    or 0 if n cannot be achieved.
    """
    if n < 2:
        return 0

    operations = 0
    current_factor = 2

    while n > 1:
        while n % current_factor == 0:
            operations += current_factor
            n //= current_factor
        current_factor += 1

    return operations

if __name__ == "__main__":
    print("Min # of operations to reach 4 char:", minOperations(4))
    print("Min # of operations to reach 12 char:", minOperations(12))
