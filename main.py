import pygame
from game import Game
import sys

pygame.init()
pygame.display.set_caption("Last Stand")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((237, 232, 208))

clock = pygame.time.Clock()
game = Game(screen)

running = True

while running:
    dt = clock.tick(60) / 1000.0

    game.handle_events()
    game.update_movement(dt)
    pygame.display.flip()

pygame.quit()
sys.exit()


