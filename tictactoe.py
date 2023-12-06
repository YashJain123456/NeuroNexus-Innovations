import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to make a move for the AI player using the Minimax algorithm
def minimax(board, depth, maximizing_player):
    if check_winner(board, "X"):
        return -1
    elif check_winner(board, "O"):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to make a move for the AI player
def ai_move(board):
    best_move = None
    best_eval = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to play the Tic-Tac-Toe game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = random.choice(["X", "O"])

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not (check_winner(board, "X") or check_winner(board, "O") or is_board_full(board)):
        if player_turn == "X":
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                player_turn = "O"
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is making a move...")
            ai_row, ai_col = ai_move(board)
            board[ai_row][ai_col] = "O"
            player_turn = "X"

        print_board(board)

    if check_winner(board, "X"):
        print("You win!")
    elif check_winner(board, "O"):
        print("AI wins!")
    else:
        print("It's a draw!")

# Start the game
play_game()
