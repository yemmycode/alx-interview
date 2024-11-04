#!/usr/bin/python3
"""
Module for finding solutions to the N queens problem.
"""
import sys

# Global variables
solutions = []  # Stores all valid solutions to the N queens problem
n = 0           # Size of the chessboard
pos = None      # List of potential positions on the chessboard

def get_input():
    """
    Retrieves and validates the program's input argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(pos0, pos1):
    """
    Determines if two queens are attacking each other.

    Args:
        pos0 (list or tuple): The position of the first queen.
        pos1 (list or tuple): The position of the second queen.

    Returns:
        bool: True if the queens are in an attacking position, otherwise False.
    """
    return (pos0[0] == pos1[0] or pos0[1] == pos1[1] or 
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))

def group_exists(group):
    """
    Checks if a given group already exists in the list of solutions.

    Args:
        group (list of lists): A group of queen positions.

    Returns:
        bool: True if the group exists in solutions, otherwise False.
    """
    global solutions
    for existing_solution in solutions:
        matches = sum(1 for pos1 in existing_solution for pos2 in group 
                      if pos1[0] == pos2[0] and pos1[1] == pos2[1])
        if matches == n:
            return True
    return False

def build_solution(row, group):
    """
    Recursively builds and checks solutions for the N queens problem.

    Args:
        row (int): The current row being processed.
        group (list of lists): The current group of queen positions.
    """
    global solutions, n
    if row == n:
        temp_group = group.copy()
        if not group_exists(temp_group):
            solutions.append(temp_group)
    else:
        for col in range(n):
            index = (row * n) + col
            new_position = pos[index].copy()
            group.append(new_position)
            if not any(is_attacking(new_position, queen) for queen in group[:-1]):
                build_solution(row + 1, group)
            group.pop()

def get_solutions():
    """
    Generates solutions for the N queens problem based on the input size.
    """
    global pos, n
    pos = [[i // n, i % n] for i in range(n ** 2)]
    build_solution(0, [])

# Main execution
n = get_input()
get_solutions()
for solution in solutions:
    print(solution)

