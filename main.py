import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Last Stand")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((237, 232, 208))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()