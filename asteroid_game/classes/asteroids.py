import pygame
import random
from asteroid_game.config import *
from asteroid_game.classes.entity import Entity

class Asteroid(Entity):
    def __init__(self, size, spawn):
        super().__init__()
        self.size = size
        self.spawn_at = spawn
        self.sprite_id = f"{random.randint(0, 47)}_{self.size}_asteroid_{self.sprite_id}"

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        #looks stupid but is needed
        if not "shot" in other.sprite_id:
            if self.col_exempt > 0:
                self.col_exempt = COL_EXEMPT
                return

        self.col_exempt = COL_EXEMPT
            
        if "asteroid" in other.sprite_id:
            if self.size > other.size:
                return
            elif self.size < other.size:
                return self.split()
            else:
                #bounce in opposite direction
                self.velocity *= -1
        else:
            return self.split()
        
    def split(self):
        if self.size <= 1:
            return "kill"

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        #for split asteroids we don't use spawn variable, we will work out pos in logic
        a1 = Asteroid(self.size - 1, None)
        a2 = Asteroid(self.size - 1, None)
        
        a1.velocity = a * 1.2
        a2.velocity = b * 1.2

        return (self.sprite_id, a1.sprite_id, a2.sprite_id)
        
        
