import pygame
from tictactoe.constants import *

class Move:
    # Constructor
    def __init__(self, player, row, col):
        self.player = player
        self.row = row
        self.col = col

    # Getters
    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getPlayer(self):
        return self.player

    # Drawing
    def draw(self, win):
        if self.player == 'x':
            start1 = (BOARD_PADDING_X + self.col * SQUARE_SIZE + MOVE_PADDING_X, BOARD_PADDING_Y + self.row *SQUARE_SIZE + MOVE_PADDING_X)
            end1 = (BOARD_PADDING_X + (self.col + 1) * SQUARE_SIZE - MOVE_PADDING_X, BOARD_PADDING_Y + (self.row + 1) * SQUARE_SIZE - MOVE_PADDING_X)
            pygame.draw.line(win, SYDELL, start1, end1, MOVE_DRAW_WEIGHT+5)

            start2 = (BOARD_PADDING_X + self.col * SQUARE_SIZE + MOVE_PADDING_X, BOARD_PADDING_Y + (self.row + 1) * SQUARE_SIZE - MOVE_PADDING_X)
            end2 = (BOARD_PADDING_X + (self.col + 1) * SQUARE_SIZE - MOVE_PADDING_X, BOARD_PADDING_Y + (self.row) * SQUARE_SIZE + MOVE_PADDING_X)
            pygame.draw.line(win, SYDELL, start2, end2, MOVE_DRAW_WEIGHT+5)
        else:
            center = (BOARD_PADDING_X + self.col * SQUARE_SIZE + SQUARE_SIZE // 2, BOARD_PADDING_Y + self.row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(win, NAVY, center, SQUARE_SIZE//2 - MOVE_PADDING_O)
            pygame.draw.circle(win, WHITE, center, SQUARE_SIZE//2 - MOVE_PADDING_O - MOVE_DRAW_WEIGHT)