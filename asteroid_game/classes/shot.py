import pygame
from asteroid_game.classes.entity import Entity

class Shot(Entity):
    def __init__(self, rot):
        super().__init__()

        self.sprite_id = "shot_" + self.sprite_id
        self.rotation = rot
        self.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * 500

    def collision(self, other):
        if "asteroid" in other.sprite_id:
            return "kill"

        



    