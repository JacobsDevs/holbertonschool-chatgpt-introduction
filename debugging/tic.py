#!/usr/bin/python3

def print_board(board):
    """
    Prints the current Tic-Tac-Toe board in a user-friendly format.
    
    Parameters:
    board (list): A 3x3 list representing the Tic-Tac-Toe board.
    
    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the Tic-Tac-Toe board.
    
    Parameters:
    board (list): A 3x3 list representing the Tic-Tac-Toe board.
    
    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows and columns
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Checks if the Tic-Tac-Toe board is full (i.e., no empty spaces left).
    
    Parameters:
    board (list): A 3x3 list representing the Tic-Tac-Toe board.
    
    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function that runs the Tic-Tac-Toe game. It alternates turns between 
    player "X" and "O" and checks for a winner or a tie. The game continues
    until there is a winner or a tie.
    
    Parameters:
    None
    
    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize the board
    player = "X"  # Player X starts
    while True:
        print_board(board)
        try:
            # Get user input with validation
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Validate row and column input
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be between 0 and 2. Try again.")
                continue

            # Check if the spot is available
            if board[row][col] == " ":
                board[row][col] = player  # Make the move
            else:
                print("That spot is already taken! Try again.")
                continue

            # Check if there's a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Check if the board is full (tie)
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch players
            player = "O" if player == "X" else "X"
        
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

if __name__ == "__main__":
    tic_tac_toe()

