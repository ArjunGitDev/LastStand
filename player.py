import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()

        self.width = 20
        self.height = 20

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.fill((18, 23, 47))

        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.position = pygame.Vector2(start_x, start_y)

        self.speed = 100

    def update_movement(self, dt, walls):
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

        velocity = direction * self.speed * dt

        self.position.x += velocity.x
        self.rect.centerx = round(self.position.x)
        for wall in walls:
            if self.rect.colliderect(wall):
                if velocity.x > 0:
                    self.rect.right = wall.left
                elif velocity.x < 0:
                    self.rect.left = wall.right
                self.position.x = self.rect.centerx

        self.position.y += velocity.y
        self.rect.centery = round(self.position.y)
        for wall in walls:
            if self.rect.colliderect(wall):
                if velocity.y > 0:
                    self.rect.bottom = wall.top
                elif velocity.y < 0:
                    self.rect.top = wall.bottom
                self.position.y = self.rect.centery
