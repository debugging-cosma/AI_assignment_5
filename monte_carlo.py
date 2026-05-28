import random

board = [
    "X", "O", " ",
    " ", "O", " ",
    "X", " ", " "
]

moves = []

for i in range(9):
    if board[i] == " ":
        wins = 0

        for _ in range(20):
            if random.choice([True, False]):
                wins += 1

        moves.append((i, wins))

best_move = max(moves, key=lambda x: x[1])

print("Best move:", best_move[0])
print("Win score:", best_move[1])