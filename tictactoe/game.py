import pygame
import random
from tictactoe.board import Board
from tictactoe.move import Move
from tictactoe.constants import *
from tictactoe.tree import Node, Tree

class Game:
    def __init__(self):
        self.turnCount = 0
        self.board = Board()
        self.gameOver = False
        self.winner = None
        self.winLine = []

    def draw(self, win):
        self.board.draw(win)
        for lines in self.winLine:
            pygame.draw.line(win,GREEN, lines[0], lines[1], 10)

    def makeMove(self, row, col):
        player = 'x' if self.turnCount % 2 == 0 else 'o'
        moveMade = Move(player, row, col)
        self.board.update(moveMade)
        if self.isWinningMove(moveMade):
            print ("Win!")
            self.gameOver = True
            self.winner = player
        if self.turnCount == 8:
            self.gameOver = True
        self.turnCount += 1
    
    def isWinningMove(self, move):
        #check same row, check same column, check diagonal
        player = move.getPlayer()
        self.winLine = self.board.isWin(player, move)
        if len(self.winLine) == 0:
            return False
        else: 
            return True

    def isGameOver(self):
        return self.gameOver

    def isValid(self, row, col):
        if self._isInRange(row, col):
            if self.board.isPosEmpty(row, col):
                return True
        return False

    def _isInRange(self, row, col):
        return (row < ROWS and row >= 0 and col < COLS and col >= 0)

    def getWinner(self):
        return self.winner

    def playAITurn(self):
        while True:
            row, col = random.randint(0,2), random.randint(0,2)
            if self.board.isPosEmpty(row, col):
                break
        player = 'x' if self.turnCount % 2 == 0 else 'o'
        movemade = Move(player, row, col)
        self.board.update(movemade)
        if self.isWinningMove(movemade):
            self.gameOver = True
            self.winner = player
        if self.turnCount == 8:
            self.gameOver = True
        self.turnCount+=1
