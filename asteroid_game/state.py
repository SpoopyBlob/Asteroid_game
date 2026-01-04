import pygame

class Sprite_Metadata():
    def __init__(self, sprite_id, x, y):
        self.id = sprite_id
        self.pos = pygame.Vector2(x, y)
        self.rot = 0
        self.mask = None
        self.alive = True
        self.col_type = "n/a"

class State():
    def __init__(self, player_id, metadate):
        self.state_dict = {}
        self.state_dict[player_id] = metadate

    def get_state(self):
        return self.state_dict.copy()
    
    def set_state(self, updated_state):
        self.state_dict = updated_state


    

    


        