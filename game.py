import pygame
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bounds = screen.get_rect()
        self.running = True

        self.player = Player(self.bounds.centerx, self.bounds.centery)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        self.player.update_movement(dt, self.bounds.width, self.bounds.height)

    def draw(self):
        self.screen.fill((237, 232, 208))
        self.all_sprites.draw(self.screen)
