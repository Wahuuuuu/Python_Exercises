"""
Author: Wahuuuuu
Version: 2.0
"""

def main() -> None:
    n = int(input("An integer: "))

    solve(n)


def solve(n: int) -> None:
    chess_board: list[int] = [0] * n

    def dfs(chess_board: list[int], placement: int) -> None:
        """
        Parameters
        ---
        chess_board: 
            It's length is n, every element of it represents a row in the chessboard, start from 0.
            And the value of the element is the column that the queen is placed.
                Ex: chess_board[6, 0] -> There are two queens on the keyboard, one on the row 0 column 6; another on the row 1 column 0.
        placement: the number of column which needs to be placed
        """
        if placement >= n and legal(chess_board):
            output(chess_board)
            return

        for i in range(n):
            chess_board[placement] = i

            if legal(chess_board[: placement + 1]):
                dfs(chess_board, placement + 1)

    dfs(chess_board, 0)


def legal(chess_board: list[int]) -> bool:

    # one queen every column and row
    rule1: bool = len(set(chess_board)) == len(chess_board)

    existed_diagonal_rl: set[int] = {i - chess_board[i] for i in range(len(chess_board) - 1)}
    existed_diagonal_lr: set[int] = {i + chess_board[i] for i in range(len(chess_board) - 1)}
    rule2 = (
        (len(chess_board)-1) - chess_board[-1] not in existed_diagonal_rl and
        (len(chess_board)-1) + chess_board[-1] not in existed_diagonal_lr
    )

    return rule1 and rule2

def output(m):
    for i in m:
        for j in range(len(m)):
            print("O" if i != j else "Q", end = " ")
        print()
    print()


main()
    
