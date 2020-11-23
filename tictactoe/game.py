from tictactoe.board import Board
from tictactoe.move import Move

class Game:
    def __init__(self):
        self.turnCount = 0
        self.board = Board()

    def draw(self, win):
        self.board.draw(win)

    def makeMove(self, row, col):
        player = 'x' if self.turnCount % 2 == 0 else 'o'
        moveMade = Move(player, row, col)
        self.board.update(moveMade)
        self.turnCount += 1
