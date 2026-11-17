import pygame
import sys

class Game:
    def __init__(self, screen):
        self.running = True

        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.player_width = 50
        self.player_height = 50

        self.player_sprite = pygame.Rect(
            self.screen_width // 2,
            self.screen_height // 2,
            self.player_width,
            self.player_height
        )

        self.player_speed = 100

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def update_movement(self, dt):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1

        self.player_sprite.x += dx * self.player_speed * dt
        self.player_sprite.y += dy * self.player_speed * dt

        pygame.draw.rect(self.screen, (0, 255, 200), self.player_sprite)