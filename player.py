import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()

        self.width = 50
        self.height = 50

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.fill((20, 20, 20))

        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.position = pygame.Vector2(start_x, start_y)

        self.speed = 400

    def update_movement(self, dt, screen_width, screen_height):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1

        direction = pygame.Vector2(dx, dy)
        if direction.length_squared() > 0:
            direction.normalize_ip()

        self.position += direction * self.speed * dt
        self.rect.center = (self.position.x, self.position.y)
