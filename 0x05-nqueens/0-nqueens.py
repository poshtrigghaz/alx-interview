#!/usr/bin/python3
"""AAAA"""

import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solutions.append([[r, c] for r, row in enumerate(board) for c, val in enumerate(row) if val])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
