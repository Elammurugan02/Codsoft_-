# TIC-TAC-TOE AI
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    scores = {"X": 1, "O": -1, "tie": 0}

    if check_winner(board, "X"):
        return scores["X"]
    if check_winner(board, "O"):
        return scores["O"]
    if is_board_full(board):
        return scores["tie"]

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Fix missing closing parenthesis here
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        x, y = map(int, input("Enter your move (row and column, e.g., '1 1'): ").split())
        if board[x - 1][y - 1] == " ":
            board[x - 1][y - 1] = "O"
            print_board(board)
        else:
            print("That cell is already occupied. Try again.")
            continue

        if check_winner(board, "O"):
            print("You win! Congratulations!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        print("AI is making its move...")
        x, y = best_move(board)
        board[x][y] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()