import pygame
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bounds = screen.get_rect()
        self.running = True

        self.wall_thickness = 20
        self.walls = [
            pygame.Rect(0, 0, self.bounds.width, self.wall_thickness),
            pygame.Rect(0, self.bounds.height - self.wall_thickness, self.bounds.width, self.wall_thickness),
            pygame.Rect(0, 0, self.wall_thickness, self.bounds.height),
            pygame.Rect(self.bounds.width - self.wall_thickness, 0, self.wall_thickness, self.bounds.height),
        ]

        self.player = Player(self.bounds.centerx, self.bounds.centery)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        self.player.update_movement(dt, self.walls)

    def draw(self):
        self.screen.fill((237, 232, 208))
        for wall in self.walls:
            pygame.draw.rect(self.screen, (0, 0, 0), wall)
        self.all_sprites.draw(self.screen)
