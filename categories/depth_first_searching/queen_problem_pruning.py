"""
Author: Wahuuuuu
---
Objective:
This code solve the queen problem with dfs with pruning
---
Input: an integer n
Output: matrixes representing the resolutions of the queen problem of size n
"""

def main() -> None:
    n = input("An integer n: ")

    solve_queen(int(n))


def solve_queen(n: int) -> None:
    chess_board: list[int] = [0] * n

    def dfs(chess_board: list[int], placement: int):
        """
        Objecive: place a queen at the placement-th row of the chessboard, while every queen before the placement-th row is well placed
            if the chess_board is fully placed, check the placement: if it's legal, output; if not, end the method.
        ---
        Parameters:
            chess_board: list[int]
                chess_board[i] == j means the queen of the i-th row is at j-th column
                every queen before the chess_board[placement] is well-placed
            placement: int
                the chess_board needs a queen to be placed on the placement-th row, didn't know which column yet

        Return: none
        """
        # basic case
        if placement >= n and legal_placement(chess_board): 
            output(chess_board)
            return

        # dfs() call and its condition
        for i in range(n):
            chess_board[placement] = i

            if legal_placement(chess_board[:placement+1]):
                dfs(chess_board, placement + 1)

    dfs(chess_board, 0)


def legal_placement(chess_board: list[int]) -> bool:
    """
    Returns whether the last placement is legal
    ---
    Parameters:
        chess_board: list[int]
            chess_board[i] == j means the queen of the i-th row is at j-th column
            every queen before the chess_board[placement] are legal
    ---
    Return: True if the last placement is legal; False otherwise
    """
    rule1: bool = len(set(chess_board)) == len(chess_board)  # one queen at every column and row

    existed_diagonal_lr: set[int] = {abs(i + chess_board[i]) for i in range(len(chess_board) - 1)}
    existed_diagonal_rl: set[int] = {i - chess_board[i] for i in range(len(chess_board) - 1)}

    rule2: bool = (
        abs(len(chess_board)-1 + chess_board[-1]) not in existed_diagonal_lr and 
        (len(chess_board)-1 - chess_board[-1] not in existed_diagonal_rl)
    )  # one queen at every diagonal
    
    return rule1 and rule2


def output(m: list[int]) -> None:
    """
    Prints a matrix represented with a list[int].
    ---
    Parameters:
        m: list[int]
    ---
    Example:
    [0, 1, 2, 3]
    q O O O 
    O q O O 
    O O q O
    O O O q
    """
    for i in m:
        for j in range(len(m)):
            print("q" if j == i else "O", end = " ")
        print()
    print()


main()