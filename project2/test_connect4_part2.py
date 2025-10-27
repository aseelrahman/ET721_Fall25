# test_connect4_part2.py
import unittest
from unittest.mock import patch
from io import StringIO
from main import Connect4


class TestPlayGame(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '2', '3'])
    def test_game_start_and_win_message(self, mock_input, mock_stdout):
        game = Connect4()
        with patch.object(game, 'check_win', side_effect=[False, False, True]):
            with patch.object(game, 'is_full', return_value=False):
                with patch.object(game, 'drop_chip', return_value=True):
                    game.play_game()
        out = mock_stdout.getvalue()
        self.assertIn("Welcome to Connect 3!", out)
        self.assertIn("Player X wins!", out)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['abc', '1'])
    def test_invalid_input(self, mock_input, mock_stdout):
        game = Connect4()
        with patch.object(game, 'check_win', side_effect=[True]):
            with patch.object(game, 'is_full', return_value=False):
                with patch.object(game, 'drop_chip', return_value=True):
                    game.play_game()
        out = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter a number between 1 and 7.", out)
        self.assertIn("wins!", out)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_full_board_tie(self, mock_input, mock_stdout):
        game = Connect4()
        with patch.object(game, 'check_win', return_value=False):
            with patch.object(game, 'is_full', return_value=True):
                with patch.object(game, 'drop_chip', return_value=True):
                    game.play_game()
        out = mock_stdout.getvalue()
        self.assertIn("It's a tie! No more moves left.", out)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '2'])
    def test_player_switch(self, mock_input, mock_stdout):
        game = Connect4()
        with patch.object(game, 'check_win', side_effect=[False, True]):
            with patch.object(game, 'is_full', return_value=False):
                with patch.object(game, 'drop_chip', return_value=True):
                    game.play_game()
        out = mock_stdout.getvalue()
        self.assertIn("Player X's turn.", out)
        self.assertIn("Player O's turn.", out)


if __name__ == '__main__':
    unittest.main()

"""
Summary of What I Tested:
- test_game_start_and_win_message: checked that “Welcome to Connect 3!” shows and Player X wins.
- test_invalid_input_then_win: tested that wrong input shows an error and the game keeps going.
- test_full_board_tie: made sure the game says it’s a tie when the board is full.
- test_player_switch: checked that turns switch between Player X and Player O.

Notes:
I used mock input() to pretend player moves and captured the printed output to check messages.
I also mocked some methods (drop_chip, check_win, is_full, print_board) to control how the game ends.
The welcome message in my code says “Connect 3!” with color, so I just looked for that text.
All tests passed successfully.
"""