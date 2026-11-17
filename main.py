import sys
import pygame
from game import Game

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1080
FPS = 60

def main():
    pygame.init()
    pygame.display.set_caption("Last Stand")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    game = Game(screen)

    while game.running:
        dt = min(clock.tick(FPS) / 1000.0, 0.05)

        game.handle_events()
        game.update(dt)
        game.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
