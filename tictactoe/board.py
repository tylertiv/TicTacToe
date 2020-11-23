import pygame
from tictactoe.constants import *
from tictactoe.move import Move

class Board:
    def __init__(self):
        self.board = [[None for row in range(ROWS)] for col in range(COLS)]
        self.moves = []

    def draw(self, win):
        win.fill(WHITE)
        for i in range(1, 3):
            pygame.draw.line(win, BLACK, (BOARD_PADDING_X + i * SQUARE_SIZE, BOARD_PADDING_Y),
                                         (BOARD_PADDING_X + i*SQUARE_SIZE, BOARD_PADDING_Y + BOARD_HEIGHT), width=5)
            pygame.draw.line(win, BLACK, (BOARD_PADDING_X, BOARD_PADDING_Y + i * SQUARE_SIZE), 
                                         (BOARD_PADDING_X + BOARD_WIDTH, BOARD_PADDING_Y + i * SQUARE_SIZE), width = 5)

        for move in self.moves:
            move.draw(win)
    
    def isPosEmpty(self, row, col):
        return (self.board[row][col] == 0)

    def update(self, move):
        self.board[move.getRow()][move.getCol()] = move.getPlayer()
        self.moves.append(move)
        print(self.board)
