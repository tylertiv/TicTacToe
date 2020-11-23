from tictactoe.board import Board
from tictactoe.move import Move
from tictactoe.constants import ROWS, COLS

class Game:
    def __init__(self):
        self.turnCount = 0
        self.board = Board()
        self.won = False
        self.winner = None

    def draw(self, win):
        self.board.draw(win)

    def makeMove(self, row, col):
        player = 'x' if self.turnCount % 2 == 0 else 'o'
        moveMade = Move(player, row, col)
        self.board.update(moveMade)
        if self.isWinningMove(moveMade):
            print ("Win!")
            self.won = True
            self.winner = player
        self.turnCount += 1

    
    def isWinningMove(self, move):
        #check same row, check same column, check diagonal
        player = move.getPlayer()
        return self.board.isWin(player, move)

    def isWon(self):
        return self.won

    def isValid(self, row, col):
        if self._isInRange(row, col):
            if self.board.isPosEmpty(row, col):
                return True
        return False

    def _isInRange(self, row, col):
        return (row < ROWS and row >= 0 and col < COLS and col >= 0)

    def getWinner(self):
        return self.winner
