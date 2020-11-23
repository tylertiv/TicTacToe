import pygame
from tictactoe.constants import WIDTH, HEIGHT
from tictactoe.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

game = Game()

def main():
    run = True
    clock = pygame.time.Clock()
    temp = 0
    while run:
        clock.tick(FPS)       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.makeMove(0, temp)
                temp +=1
        run = False if temp == 4 else True
        game.draw(WIN)
        pygame.display.update()

main()
