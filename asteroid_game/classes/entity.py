import pygame
import uuid

class Entity(pygame.sprite.Sprite):

    def __init__(self):
        if hasattr(self, "entities"):
            super().__init__(self.entities)
        else:
            super().__init__()

        self.velocity = pygame.Vector2(0, 0)
        self.sprite_id = str(uuid.uuid4())

