import unittest

from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Initialize a game instance before each test."""
        self.game = TicTacToe()

    def test_initial_board(self):
        """Test if the board initializes correctly."""
        expected_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, expected_board)

    def test_valid_moves(self):
        """Test valid moves."""
        self.game.make_move(1)
        self.assertEqual(self.game.board[0][0], 'X')  # Player X's move
        self.game.make_move(5)
        self.assertEqual(self.game.board[1][1], 'X')  # Player X's move

    def test_invalid_move(self):
        """Test that an invalid move raises an error."""
        self.game.make_move(1)
        self.assertRaises(ValueError, self.game.make_move, 1)  # Trying to occupy an already filled cell

    def test_winning_condition_rows(self):
        """Test winning condition for rows."""
        self.game.make_move(1)  # X
        self.game.switch_player()
        self.game.make_move(2)  # O
        self.game.switch_player()
        self.game.make_move(4)  # X
        self.game.switch_player()
        self.game.make_move(5)  # O
        self.game.switch_player()
        self.game.make_move(7)  # X
        self.assertEqual(self.game.check_winner(), 'X')

    def test_winning_condition_columns(self):
        """Test winning condition for columns."""
        self.game.make_move(1)  # X
        self.game.switch_player()
        self.game.make_move(4)  # O
        self.game.switch_player()
        self.game.make_move(2)  # X
        self.game.switch_player()
        self.game.make_move(5)  # O
        self.game.switch_player()
        self.game.make_move(3)  # X
        self.assertEqual(self.game.check_winner(), 'X')

    def test_winning_condition_diagonal(self):
        """Test winning condition for diagonals."""
        self.game.make_move(1)  # X
        self.game.switch_player()
        self.game.make_move(2)  # O
        self.game.switch_player()
        self.game.make_move(5)  # X
        self.game.switch_player()
        self.game.make_move(4)  # O
        self.game.switch_player()
        self.game.make_move(9)  # X
        self.assertEqual(self.game.check_winner(), 'X')

    def test_tie_condition(self):
        """Test for a tie condition."""
        moves = [1, 2, 3, 5, 4, 6, 8, 7, 9]  # Filling the board without a winner
        for move in moves:
            self.game.make_move(move)
            if move != moves[-1]:
                self.game.switch_player()  # Switch for next player's turn
        self.assertIsNone(self.game.check_winner())  # No winner
        self.assertEqual(self.game.print_board(), None)  # This line is just to avoid printing in test


if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main()
