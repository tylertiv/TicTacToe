import pygame
from tictactoe.constants import *
from tictactoe.move import Move

class Board:
    def __init__(self, boardState = None):
        if boardState is None:
            self.board = [[None for row in range(ROWS)] for col in range(COLS)]
            self.moves = []
    
    def draw(self, win):
        for i in range(1, 3):
            pygame.draw.line(win, BLACK, (BOARD_PADDING_X + i * SQUARE_SIZE, BOARD_PADDING_Y),
                                         (BOARD_PADDING_X + i*SQUARE_SIZE, BOARD_PADDING_Y + BOARD_HEIGHT), width=5)
            pygame.draw.line(win, BLACK, (BOARD_PADDING_X, BOARD_PADDING_Y + i * SQUARE_SIZE), 
                                         (BOARD_PADDING_X + BOARD_WIDTH, BOARD_PADDING_Y + i * SQUARE_SIZE), width = 5)
        for move in self.moves:
            move.draw(win)
    
    def isPosEmpty(self, row, col):
        return (self.board[row][col] is None)

    def update(self, move):
        self.board[move.getRow()][move.getCol()] = move.getPlayer()
        self.moves.append(move)
        print(self.board)

    def isTerminalState(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is not None:
                    count += 1
        if count == 9:
            return True

        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'x':
                    count += 1
                if self.board[i][j] == 'o':
                    count -= 1
            if abs(count) == 3:
                return True
        for i in range(3):
            for j in range(3):
                if self.board[j][i] == 'x':
                    count += 1
                if self.board[j][i] == 'o':
                    count -= 1
            if abs(count) == 3:
                return True

        return False

    def isWin(self, player, move):
        rowWin, colWin, diagWin = True, True, False
        for row in self.board:
            if row[move.getCol()] != player:
                colWin = False
        for value in self.board[move.getRow()]:
            if value != player:
                rowWin = False
        
        winList = []
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player):
            xstart, ystart = BOARD_PADDING_X, BOARD_PADDING_Y
            xend, yend = BOARD_PADDING_X + BOARD_WIDTH, BOARD_PADDING_Y + BOARD_HEIGHT
            winList.append(((xstart, ystart), (xend, yend)))
        
        if (self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player):
            xstart, ystart = BOARD_PADDING_X + BOARD_WIDTH, BOARD_PADDING_Y
            xend, yend = BOARD_PADDING_X, BOARD_PADDING_Y + BOARD_HEIGHT
            winList.append(((xstart, ystart), (xend, yend)))
        
        if rowWin:
            xstart = BOARD_PADDING_X
            ystart = BOARD_PADDING_Y + move.getRow() * SQUARE_SIZE + SQUARE_SIZE // 2
            xend = BOARD_PADDING_X + BOARD_WIDTH
            yend = ystart
            winList.append(((xstart, ystart), (xend, yend)))

        if colWin:
            xstart = BOARD_PADDING_X + move.getCol() * SQUARE_SIZE + SQUARE_SIZE // 2
            ystart = BOARD_PADDING_Y
            xend = xstart
            yend = BOARD_PADDING_Y + BOARD_HEIGHT
            winList.append(((xstart, ystart), (xend, yend)))
        return winList

