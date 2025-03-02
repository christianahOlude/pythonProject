def print_board(board):
    for index, row in enumerate(board):
        print(' | '.join(row))
        if index < 2:
            print('-' * 15)


def check_winner(board):
    #row
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    #column
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != '') or \
            (board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' '):
        return board[1][1]
    return None


def tic_tac_toe():
    # Create the board with empty spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Start with player X

    # Loop for a maximum of 9 turns
    for turn in range(9):
        print_board(board)  # Print the current board
        print(f"Player {current_player}, choose your move (1-9): ")

        # Get valid input from the player
        while True:
            try:
                move = int(input())  # Get input and convert to an integer

                # Check if the move is between 1 and 9
                if move < 1 or move > 9:
                    raise ValueError("Please enter a number between 1 and 9.")

                    # Convert the move to row and column
                row = (move - 1) // 3
                col = (move - 1) % 3

                # Check if the cell is already taken
                if board[row][col] != ' ':
                    raise ValueError("Cell already taken. Choose another.")

                    # Place the player's mark on the board
                board[row][col] = current_player
                break  # Exit the loop if the move is valid

            except ValueError as e:
                print(e)  # Print the error message and ask again

        # Check for a winner after each move
        winner = check_winner(board)
        if winner:
            print_board(board)  # Print the final board
            print(f"Player {winner} wins!")  # Announce the winner
            return  # End the game

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

        # If all turns are used and no winner, it's a tie
    print_board(board)
    print("It's a tie!")


if __name__ == '__main__':
    tic_tac_toe()