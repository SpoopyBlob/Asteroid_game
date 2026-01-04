import pygame
from asteroid_game.config import *
from asteroid_game.assets import Assets

class Render():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.assets = Assets()
        

    def draw(self, state):
        self.screen.fill((0, 0, 0))

        for sprite_id, metadate in state.items():
            if "spaceship" in sprite_id or "shot" in sprite_id:
                image = self.assets.get_img(sprite_id)
                image = pygame.transform.rotate(image, -metadate.rot)
                rect = image.get_rect()
                rect.center = metadate.pos
            else: #asteroid
                image = self.assets.get_asteroid_img(sprite_id)
                rect = self.assets.get_asteroid_rect(sprite_id)
                rect.center = metadate.pos
          
            self.screen.blit(image, rect)

        pygame.display.flip()