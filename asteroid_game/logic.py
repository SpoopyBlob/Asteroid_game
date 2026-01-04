import pygame
from asteroid_game.entity_manager import Entity_Manager
from asteroid_game.state import Sprite_Metadata


class Logic():
    def __init__(self):
        self.entity_manager = Entity_Manager()

    def update(self, state, dt):
        #handles flagged collisions, calculates new x y
        state = self.collision_calc(state.copy())
        
        #clears sprites from state, no longer in use
        state = self.clear_inactive_entities(state.copy())
        
        #updates all sprites in entity_manager
        self.entity_manager.update(dt)

        #retrieves metadate from entity manager to update state
        metadate = self.entity_manager.get_entity_metadate()

        #creates state objects for new sprites if needed
        state = self.prep_state(metadate, state.copy())

        #update .pos for entities based on velocity (.rot for entities requiring rotation variable)
        state = self.update_state(state.copy(), metadate, dt)

        return state

    def update_state(self, state, metadate, dt):
        for sprite_id, date in metadate.items():

            if "spaceship" in sprite_id or "shot" in sprite_id:
                state[sprite_id].rot = date["rot"]
            state[sprite_id].pos += (date["vel"] * dt) 

        return state        

    def return_player_id(self):
        return self.entity_manager.get_player_id()
    
    #creates state object for player: Used in main before game loop
    def init_player(self):
        return Sprite_Metadata(self.return_player_id(), 640, 360)
    

    def prep_state(self, metadate, state):
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
    #finds collisions flagged in state + reset col_type to "n/a" for next game loop
    def col_check(self, state):
        col = []
        for sprite_id in state:
            if state[sprite_id].col_type != "n/a":
                if not (state[sprite_id].col_type, sprite_id) in col:
                    col.append((sprite_id, state[sprite_id].col_type))
                state[sprite_id].col_type = "n/a"
                                              
        return col
    
    def collision_calc(self, state):
        col = self.col_check(state)
        if len(col) == 0:
            return state
        
        # executes collision behaviour on sprites
        split, kill = self.entity_manager.handle_sprite_collisions(col)
        # split = when an asteroid splits into two new asteroids
        # kill = when an entity has died
        # we communicate only these two instances as it requires updating the state
            
        if split != None:
            for sprites in split:
            
                state[sprites[0]].alive = False
                pos_x = state[sprites[0]].pos.x
                pos_y = state[sprites[0]].pos.y
            
                s_1 = self.create_obj(sprites[1], pos_x + 30, pos_y + 30)
                s_2 = self.create_obj(sprites[2], pos_x - 30, pos_y - 30)

                state[sprites[1]] = s_1
                state[sprites[2]] = s_2
            
        for sprite_id in kill:
            state[sprite_id].alive = False

        

        return state

                

        




    


   

        