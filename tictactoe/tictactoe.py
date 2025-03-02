class TicTacToe:
    def __init__(self):
        # Initialize the game board and current player
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Start with player X

    def print_board(self):
        # Print the current state of the board
        for index, row in enumerate(self.board):
            print(' | '.join(row))
            if index < 2:
                print('-' * 21)

    def check_winner(self):
        # Check rows for a winner
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

                # Check columns for a winner
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

                # Check diagonals for a winner
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ') or \
                (self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' '):
            return self.board[1][1]

        return None

    def make_move(self, move):
        # Convert the move to row and column
        row = (move - 1) // 3
        col = (move - 1) % 3

        if not self.is_valid_move(move):
            raise ValueError('invalid move pls choose an empty shell between 1-9')

        # Place the player's mark on the board
        self.board[row][col] = self.current_player

    def switch_player(self):
        # Switch the current player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_valid_move(self, move):
        # Check if the move is valid
        row = (move - 1) // 3
        col = (move - 1) % 3
        return 1 <= move <= 9 and self.board[row][col] == ' '

