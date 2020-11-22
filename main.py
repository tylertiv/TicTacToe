import pygame
from tictactoe.constants import WIDTH, HEIGHT
from tictactoe.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

game = Game()

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass #will register a click when implemented
        game.draw(WIN)
        pygame.display.update()

main()
