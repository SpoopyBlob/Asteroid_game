import pygame
import random
from asteroid_game.classes.entity import Entity

class Asteroid(Entity):
    def __init__(self, size, spawn):
        super().__init__()
        self.size = size
        self.spawn_at = spawn
        self.sprite_id = f"{random.randint(0, 47)}_{self.size}_asteroid{self.sprite_id}"
