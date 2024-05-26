#!/usr/bin/python3
'''N-Queens Puzzle Problem
'''
import sys


def solve_queens(rows, columns):
    """
    Solves the N-Queens problem
    """
    solution = [[]]
    for queen in range(rows):
        solution = place_queen(queen, columns, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Finds all safe positions to place the queen in the given column
    for the current queen.

    Args:
        queen (int): The current queen being placed.
        column (int): The column to place the queen in.
        prev_solution (list): The previous solution.

    Returns:
        list: A list of all safe positions to place the queen in the
              given column.
    """
    # Find all safe positions to place the queen in the given column
    safe_position = []
    for array in prev_solution:
        # Check if each position in the previous solution is safe
        for x in range(column):
            if is_safe(queen, x, array):
                # If it is safe, add it to the list of safe positions
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    Check if a given position (x, q) is safe to place the queen.

    Args:
        q (int): The row index.
        x (int): The column index.
        array (list): The previous solution.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check if the column is already occupied
    if x in array:
        return False
    else:
        # Check if the queen attacks any other queen
        # in the same row or diagonal
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def start():
    """
    N-Queens

    This function takes a command line argument N
    and solves the N-Queens problem. It checks if the
    argument is a number and at least 4, and then calls the
    returns the value of n.
    If the argument is not a number or less than 4, it
    prints an error message and exits the program.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def nqueens():
    """
    Entry point to solve the N-Queens problem.

    This function calls the start function to get the value
    of N, and then calls the solve_queens function to solve
    the N-Queens problem.
    """
    n = start()

    # Solve the N-Queens problem
    generate_solution = solve_queens(n, n)
    for array in generate_solution:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == "__main__":
    nqueens()
