#!/usr/bin/python3
"""
N queens puzzle solver
"""

import sys


def print_usage_and_exit(message):
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    This is checked by ensuring no other queens are in the
    same column, or on the same diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N queens puzzle and print all solutions
    Each solution is represented as a list of lists
    where each sublist [i, j] represents a queen placed
    at row i and column j
    """
    def backtrack(row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)

    solutions = []
    board = [-1] * N
    backtrack(0)
    for sol in solutions:
        print([[i, sol[i]] for i in range(N)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solve_nqueens(N)
