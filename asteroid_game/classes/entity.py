import pygame
import uuid
from asteroid_game.config import *

class Entity(pygame.sprite.Sprite):
    register = {}

    def __init__(self):
        if hasattr(self, "entities"):
            super().__init__(self.entities)
        else:
            super().__init__()
        
        self.col_exempt = COL_EXEMPT
        self.velocity = pygame.Vector2(0, 0)
        self.sprite_id = str(uuid.uuid4())
        Entity.register[self.sprite_id] = self
    
        #I use information from the sprite_id to identify type of sprite; for asteroids type_of_asteroid + size + asteroid
        #e.g. 22_3_asteroid_(id goes here) 22 = index for asteroid sprite, 3 = size | spaceship_(id_goes_here) etc...
        #I use sprite_id to identify specific sprites through the entire game loop and match them with their state object
        #For quick retrieveal of sprite objects we use the register a class variable (used mainly for collisions)
    
    def update(self, dt):
        if self.col_exempt > 0:
            self.col_exempt -= dt
    
    def unpack_id(self, sprite_id):
        sprite_id = sprite_id.split("_")
        return sprite_id[-1]

    def find_sprite(self, sprite_id):
        sprite_id = self.unpack_id(sprite_id)
        return Entity.register[sprite_id]
    
    def kill(self):
        del Entity.register[self.unpack_id(self.sprite_id)]
        self.entities.remove(self)
    
        
    


    

