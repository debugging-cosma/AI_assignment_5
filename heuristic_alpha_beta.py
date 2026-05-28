def heuristic(board):
    x_count = board.count("X")
    o_count = board.count("O")

    return x_count - o_count


def alpha_beta(board, depth, alpha, beta, is_max):
    if depth == 3:
        return heuristic(board)

    if " " not in board:
        return heuristic(board)

    if is_max:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                best = max(best,
                           alpha_beta(board, depth+1, alpha, beta, False))

                board[i] = " "

                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                best = min(best,
                           alpha_beta(board, depth+1, alpha, beta, True))

                board[i] = " "

                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best


board = [
    "X", "O", " ",
    " ", "O", " ",
    "X", " ", " "
]

print(alpha_beta(board, 0, -100, 100, True))