#!/usr/bin/python3

"""Module for N Queens"""


def position(board, row, col):
    """Checks if position is safe from attack
    Args:
        board: The board state.
        row: Row of boaded.
        col: column of board.
    """
    for i in range(col):
        if board[i] is row or abs(board[i] - row) is abs(i - col):
            return False
    return True


def Board(board, col):
    """board state using backtracking
    Args:
        board: board
        col: colum to check.
    """
    n = len(board)
    if col is n:
        print(str([[i, board[i]] for i in range(n)]))
        return

    for row in range(n):
        if position(board, row, col):
            board[col] = row
            Board(board, col + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = 0
    try:
        n = int(sys.argv[1])
    except Exception as e:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for col in range(n)]
    Board(board, 0)
