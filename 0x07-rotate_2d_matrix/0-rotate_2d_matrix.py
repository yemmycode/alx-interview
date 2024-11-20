#!/usr/bin/python3
"""Module to rotate a 2D matrix in place and output in columns.
"""

def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in place, returning column-oriented output."""
    # Confirm the input is a list
    if not isinstance(matrix, list):
        return
    
    # Exit if the matrix is empty
    if not matrix:
        return
    
    # Validate that all rows in the matrix are lists
    if not all(isinstance(row, list) for row in matrix):
        return
    
    # Determine the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Ensure all rows have equal length
    if not all(len(row) == cols for row in matrix):
        return
    
    # Prepare the rotated matrix structure
    rotated_matrix = [[] for _ in range(cols)]
    
    # Populate the rotated matrix column by column
    for col in range(cols):
        for row in range(rows - 1, -1, -1):  # Reverse the row traversal
            rotated_matrix[col].append(matrix[row][col])
    
    # Replace the original matrix with the column-oriented rotated matrix
    matrix.clear()
    matrix.extend(rotated_matrix)

