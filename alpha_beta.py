def evaluate(board):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c]:
            if board[a] == "X":
                return 1
            elif board[a] == "O":
                return -1

    return 0


def alpha_beta(board, depth, alpha, beta, is_max):
    score = evaluate(board)

    if score != 0:
        return score

    if " " not in board:
        return 0

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
    "X", "O", "X",
    " ", "O", " ",
    " ", " ", "X"
]

print(alpha_beta(board, 0, -100, 100, True))