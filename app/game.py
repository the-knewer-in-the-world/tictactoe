# app/game.py
class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [' '] * 9  # 0..8
        self.current = 'X'
        self.winner = None

    def make_move(self, pos):
        if pos < 0 or pos > 8:
            raise ValueError("pos must be 0..8")
        if self.board[pos] != ' ':
            raise ValueError("cell already used")
        self.board[pos] = self.current
        if self._check_winner(self.current):
            self.winner = self.current
        self.current = 'O' if self.current == 'X' else 'X'

    def _check_winner(self, p):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in wins:
            if self.board[a]==self.board[b]==self.board[c]==p:
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board and self.winner is None

    def state(self):
        return {'board': self.board, 'current': self.current, 'winner': self.winner}
