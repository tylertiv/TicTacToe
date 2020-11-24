import pygame
import pygame.freetype
from tictactoe.constants import *
from tictactoe.game import Game

pygame.freetype.init()
GAME_FONT = pygame.freetype.SysFont("Helvetica", 14)

RESET_BUTTON = pygame.Rect(5,5,80,30)
restart_text_surface, rect = GAME_FONT.render("RESET", BLACK, True)

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
        pygame.draw.rect(WIN, GRAY, pygame.Rect(7,7,80,30))
        pygame.draw.rect(WIN, BUTTON, RESET_BUTTON)
        
        WIN.blit(restart_text_surface, (24,14))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                click_spot = pygame.Rect(x,y,1,1)
                if RESET_BUTTON.colliderect(click_spot):
                    print("Clicked restart")
                    game = Game()
                    run = True
                    gameOver = False
                elif not gameOver:
                    row, col = calcSquare(x,y)
                    if game.isValid(row, col):
                        game.makeMove(row, col)
                        gameOver = game.isGameOver()
                        if gameOver:
                            gameOver = True
                            if game.getWinner():
                                print("Winner:", game.getWinner())
                            else:
                                print("Cat's Game")
        game.draw(WIN)
        pygame.display.update()

    
def calcSquare(x,y):
    col = (x - BOARD_PADDING_X)//SQUARE_SIZE
    row = (y - BOARD_PADDING_Y)//SQUARE_SIZE
    #print("(",row, ", " ,col,")")
    return (row, col)

main()
