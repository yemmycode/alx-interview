def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    Args:
        n (int): The number of rows of Pascal's triangle.
    
    Returns:
        list: A list of lists where each list represents a row of Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row as [1]

    for i in range(1, n):
        # Create the new row starting with [1]
        row = [1]
        
        # Compute the middle elements by summing the two values above in the triangle
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End the row with [1]
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)

    return triangle
