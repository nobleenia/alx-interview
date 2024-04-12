#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth level.

    Pascal's Triangle is constructed such that each number
    is the sum of the two numbers directly above it.
    The function returns a list of lists,
    where each inner list represents a row in the triangle.

    Parameters:
    n (int): The number of levels in the triangle.
    If n is less than or equal to 0,
    the function returns an empty list.

    Returns:
    list: A list of lists, with each inner list containing integers
    representing a row of Pascal's Triangle.
    """

    if n <= 0:
        # Return an empty list if n is not positive
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Start a new row with the first element 1
        row = [1]
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            # from the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with the last element 1
        row.append(1)
        triangle.append(row)

    return (triangle)
