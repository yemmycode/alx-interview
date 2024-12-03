#!/usr/bin/python3
"""Module for calculating the perimeter of an island.
"""

def island_perimeter(grid):
    """Calculates the perimeter of an island without any lakes.
    """
    perimeter = 0
    if not isinstance(grid, list):  # Checking if grid is a list
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            # Checking the four edges of the island cell
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
