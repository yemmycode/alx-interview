#!/usr/bin/python3
"""
Defines a function pascal_triangle(n) that returns Pascal's triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns Pascal's triangle up to n rows as a list of lists of integers.

    Args:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize Pascal's triangle with the first row [1].

    for i in range(1, n):
        # Create a new row starting with [1].
        triangle.append([1])

        # Populate the new row based on the previous row.
        for j in range(1, i):
            triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])

        # Append 1 to complete the current row.
        triangle[i].append(1)

    return triangle
