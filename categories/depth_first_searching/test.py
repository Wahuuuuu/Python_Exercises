
def main() -> None:
    O = "O"
    Q = "Q"
    love = [
        [O, O, Q, O],
        [O, Q, O, O],
        [O, O, O, Q],
        [Q, O, O, O]
    ]

    print(f"chessboard = ", end = "")
    sex:list[int] = make(love)
    for i in sex:
        print(i, end=" ")
    print()
    
    print(legal(sex))



def make(love) -> list[int]:
    sex = [i for j in love for i in range(len(j)) if j[i] == "Q"]

    return sex


def legal(chess_board: list[int]) -> bool:

    # one queen every column and row
    rule1: bool = len(set(chess_board)) == len(chess_board)

    existed_diagonal_rl: set[int] = {i - chess_board[i] for i in range(len(chess_board) - 1)}
    existed_diagonal_lr: set[int] = {i + chess_board[i] for i in range(len(chess_board) - 1)}
    for i in range(len(chess_board) - 1):
        print(i + chess_board[i])

    print(len(existed_diagonal_rl), len(existed_diagonal_lr))
    for i in existed_diagonal_rl:
        print(i, end= " ")
    print()
    for i in existed_diagonal_lr:
        print(i, end= " ")
    print()

    rule2 = (
        chess_board[-1] - len(chess_board)-1 not in existed_diagonal_rl and
        chess_board[-1] + len(chess_board)-1 not in existed_diagonal_lr
    )

    return rule1 and rule2


main()
