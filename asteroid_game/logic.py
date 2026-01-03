import pygame
from asteroid_game.entity_manager import Entity_Manager
from asteroid_game.state import Sprite_Metadata


class Logic():
    def __init__(self):
        self.entity_manager = Entity_Manager()

    def update(self, state, dt):
        #retrieves and modifies behaviour from entity manager and calculates new x y
        #state = self.collision_calc(state.copy())
        
        #clears sprites no longer in use
        state = self.clear_inactive_entities(state.copy())
        
        #updates all sprites
        self.entity_manager.update(dt)

        #retrieved metadate from entity manager to update state
        metadate = self.entity_manager.get_entity_metadate()

        #creates state objects for new sprites if needed
        state = self.update_state(metadate, state.copy())

        #update .pos for entities based on velocity
        for sprite_id, date in metadate.items():

            if "spaceship" in sprite_id or "shot" in sprite_id:
                state[sprite_id].rot = date["rot"]
            state[sprite_id].pos += (date["vel"] * dt) 

        return state

    def return_player_id(self):
        return self.entity_manager.get_player_id()
    
    def init_player(self):
        return Sprite_Metadata(self.return_player_id(), 640, 360)
    
    def update_state(self, metadate, state):
        for sprite in metadate:
            if sprite not in state:
                if "shot" in sprite:
                    pid = self.entity_manager.get_player_id()
                    forward = pygame.Vector2(0, -48).rotate(metadate[sprite]["rot"])
                    pos = state[pid].pos + forward
                    state[sprite] = self.create_obj(sprite, pos.x, pos.y)
                if "asteroid" in sprite:
                    pos = metadate[sprite]["spawn"]
                    state[sprite] = self.create_obj(sprite, pos.x, pos.y )
        return state

    def create_obj(self, sprite_id, x, y):
        return Sprite_Metadata(sprite_id, x , y)
    
    def clear_inactive_entities(self, state):
        state_copy = state.copy()

        for sprite_id, obj in state_copy.items():
            if obj.alive == False:
                self.entity_manager.del_entity(sprite_id)
                del state[sprite_id]
        
        return state
    
    def get_collisions(self, state):
        col = []
        for sprite_id in state:
            if state[sprite_id].col_type != "n/a":
                col.append(sprite_id, state[sprite_id].col_type)

        return col
    
    def collision_calc(self, state):
        col = self.get_collisions(state)

                

        




    


   

        