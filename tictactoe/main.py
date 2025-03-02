from tictactoe import TicTacToe
from tictactoe.TicTacToe import *

class Main:

    def play_game(self):
        # Main game loop
        for turn in range(9):
            self.print_board()  # Print the current board
            print(f"Player {self.current_player}, choose your move (1-9): ")

            # Get valid input from the player
            while True:
                try:
                    user_input = input()  # Get input

                    # Attempt to convert input to integer
                    if not user_input.isdigit():
                        raise ValueError("Please enter a number between 1 and 9.")

                    move = int(user_input)  # Convert to int

                    if not self.is_valid_move(move):
                        raise ValueError("Invalid move. Please choose an empty cell between 1 and 9.")

                        # Make the move
                    self.make_move(move)
                    break  # Exit the loop if the move is valid

                except ValueError as e:
                    print(e)  # Print the error message and ask again

            # Check for a winner after each move
            winner = self.check_winner()
            if winner:
                self.print_board()  # Print the final board
                print(f"Player {winner} wins!")  # Announce the winner
                return  # End the game

            # Switch players
            self.switch_player()

            # If all turns are used and no winner, it's a tie
        self.print_board()
        print("It's a tie!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()