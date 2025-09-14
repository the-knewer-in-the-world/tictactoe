# tests/test_game.py
import pytest
from app.game import TicTacToe

def test_make_move_and_turn_switch():
    g = TicTacToe()
    g.make_move(0)
    assert g.board[0] == 'X'
    assert g.current == 'O'

def test_invalid_move():
    g = TicTacToe()
    g.make_move(0)
    with pytest.raises(ValueError):
        g.make_move(0)  # same cell

def test_winner_row():
    g = TicTacToe()
    g.board = ['X','X','X',' ',' ',' ',' ',' ',' ']
    assert g._check_winner('X')  # internal check used for test

