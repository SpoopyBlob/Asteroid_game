import pygame
from asteroid_game.config import *
from asteroid_game.classes.entity import Entity
from asteroid_game.classes.shot import Shot

class Spaceship(Entity):
    def __init__(self):
        super().__init__()
        self.sprite_id = "spaceship" + self.sprite_id
        self.rotation = 0
        self.acceleration = 0
        self.shot_cooldown = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_w]:
            self.move(-1, dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(1, dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.velocity -= self.velocity * DRAG * dt

        if self.velocity.length() > MAX_SPEED:
            self.velocity.scale_to_length(MAX_SPEED)

    def rotate(self, dt):
        self.rotation += SHIP_TURN * dt

    def move(self, mod, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        self.acceleration = forward * SHIP_THRUST * mod
        self.velocity += self.acceleration * dt   

    def shoot(self):
        if self.shot_cooldown < 0:
            self.shot_cooldown = SHOT_COOLDOWN
            Shot(self.rotation)
