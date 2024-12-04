#!/usr/bin/python3
"""Module for calculating the perimeter of an island.

This module defines a function that calculates the perimeter of an island
represented by a grid of land and water. The island is surrounded by water,
and the perimeter is computed based on the edges of land cells.
"""

def island_perimeter(grid):
    """Calculates the perimeter of an island without any lakes.

    Args:
        grid (list of list of int): A 2D list representing a map of the island.
            Land is represented by 1, and water is represented by 0.

    Returns:
        int: The perimeter of the island.
            If the grid is not a valid list of lists or is empty, returns 0.
    """
    perimeter = 0

    # Validate input
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
