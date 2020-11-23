import pygame
from tictactoe.constants import *
from tictactoe.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    game = Game()
    run = True
    gameOver = False
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)    
        WIN.fill(WHITE)   
        pygame.draw.rect(WIN, GRAY, pygame.Rect(5,5,100,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                pos = pygame.mouse.get_pos()      
                row, col = calcSquare(pos)
                if game.isValid(row, col):
                    game.makeMove(row, col)
                    if game.isWon():
                        print("It's ova,", game.getWinner(), "wins!")
                        gameOver = True
            """if event.type == pygame.MOUSEBUTTONDOWN and gameOver:
                if """

        game.draw(WIN)
        pygame.display.update()

def calcSquare(pos):
    col = (pos[0] - BOARD_PADDING_X)//SQUARE_SIZE
    row = (pos[1] - BOARD_PADDING_Y)//SQUARE_SIZE
    print("(",row, ", " ,col,")")
    return (row, col)

main()
