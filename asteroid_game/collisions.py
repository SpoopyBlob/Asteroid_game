import pygame
from asteroid_game.config import *
from asteroid_game.assets import Assets

class Collision():
    def __init__(self):
        self.assets = Assets()
    
    def update(self, state):
        #checks for sprites off screen, flags them for deletion
        state = self.out_of_bounds_check(state.copy())
        
        #soft collision check, checks rect objects first (AABB collisions)
        #rects are less resource heavy then masks
        collisions = self.soft_collision_check(state)

        #check for mask collisions (masks provide pixel perfect collision detection)
        state = self.mask_collision_check(collisions, state.copy())

        return state
    
    def out_of_bounds_check(self, state):
        for sprite_id, data in state.items():
            pos = data.pos

            if pos.x < -OUT_OF_BOUNDS_LIMIT or pos.x > SCREEN_WIDTH + OUT_OF_BOUNDS_LIMIT:
                state[sprite_id].alive = False
                continue
            if pos.y < -OUT_OF_BOUNDS_LIMIT or pos.y > SCREEN_HEIGHT + OUT_OF_BOUNDS_LIMIT:
                state[sprite_id].alive = False
                continue
        
        return state

    def soft_collision_check(self, state):
        collision = []
        for sprite in state:
            sprite_rect = self.assets.get_rect(sprite)
            sprite_rect.center = state[sprite].pos

            for sprite_2 in state:

                if sprite == sprite_2:
                    continue

                sprite_rect_2 = self.assets.get_rect(sprite_2)
                sprite_rect_2.center = state[sprite_2].pos

                if sprite_rect.colliderect(sprite_rect_2):
                    if not (sprite_2, sprite) in collision:
                        if "spaceship" in sprite or "spaceship" in sprite_2:
                            if "shot" in sprite or "shot" in sprite_2:
                                continue
                            
                        collision.append((sprite, sprite_2))   

        return tuple(collision)                            

    def mask_collision_check(self, collisions, state):
        for col in collisions:
            img_1 = self.assets.get_img(col[0])
            img_2 = self.assets.get_img(col[1])

            rect_1 = None
            rect_2 = None

            mask_1 = None
            mask_2 = None

            if "spaceship" in col[0] or "shot" in col[0]:
                img_1 = pygame.transform.rotate(img_1, state[col[0]].rot)
                rect_1 = img_1.get_rect()
                mask_1 = pygame.mask.from_surface(img_1)
            else:
                rect_1 = self.assets.get_rect(col[0])
                mask_1 = self.assets.get_asteroid_mask(col[0])

            if "spaceship" in col[1] or "shot" in col[1]:
                img_2 = pygame.transform.rotate(img_2, state[col[1]].rot)
                rect_2 = img_2.get_rect()
                mask_2 = pygame.mask.from_surface(img_2)
            else:
                rect_2 = self.assets.get_rect(col[1])
                mask_2 = self.assets.get_asteroid_mask(col[1])

            rect_1.center = state[col[0]].pos
            rect_2.center = state[col[1]].pos
            
            offset = (
                rect_1.left - rect_2.left,
                rect_1.top - rect_2.top
            )
            
            if mask_2.overlap(mask_1, offset) is not None:
                state[col[0]].col_type = col[1]
                state[col[1]].col_type = col[0]

        return state

        





