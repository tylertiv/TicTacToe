import pygame
from tictactoe.constants import *

class Board:
    def __init__(self):
        self.board = []

    def draw(self, win):
        win.fill(WHITE)
        for i in range(1, 3):
            pygame.draw.line(win, BLACK, (BOARD_PADDING_X + i * SQUARE_SIZE, BOARD_PADDING_Y), (BOARD_PADDING_X + i*SQUARE_SIZE, HEIGHT - BOARD_PADDING_Y), width=5)
            pygame.draw.line(win, BLACK, (BOARD_PADDING_X, BOARD_PADDING_Y + i * SQUARE_SIZE), (BOARD_PADDING_X + BOARD_WIDTH, BOARD_PADDING_Y + i * SQUARE_SIZE), width = 5)
        