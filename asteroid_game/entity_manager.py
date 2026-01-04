import pygame
from asteroid_game.classes.spaceship import Spaceship
from asteroid_game.classes.entity import Entity
from asteroid_game.classes.asteroid_spawn import Asteroid_Spawn

class Entity_Manager():
    def __init__(self):
        self.entities = pygame.sprite.Group()
        Entity.entities = self.entities
        self.player = Spaceship()
        self.asteroid_spawn = Asteroid_Spawn()

    def update(self, dt):
        self.entities.update(dt)
        self.asteroid_spawn.update(dt)

    def get_entity_metadate(self):
        metadate = {}
        for entity in self.entities:
            sprite_id = entity.sprite_id
            package = {}
    
            if "spaceship" in sprite_id or "shot" in sprite_id:
                package["rot"] = entity.rotation
                
            if "asteroid" in sprite_id:
                package["spawn"] = entity.spawn_at

            package["vel"] = entity.velocity

            metadate[sprite_id] = package

        return metadate
    
    def get_player_id(self):
        return self.player.sprite_id
    
    def del_entity(self, sprite_id):
        for entity in self.entities:
            if entity.sprite_id == sprite_id:
                self.entities.remove(entity)
                del entity
           
    def handle_sprite_collisions(self, col):
        #split_collisions is when an asteroid splits into two
        #we need to communicate with the logic module in this cirumstance as we need to alter the .pos vector in state
        #same goes for sprites_to_kill, we need to comunicate with state
        split_collisions = []
        sprites_to_kill = set()
        
        for sprite in col:
            sprite_1 = self.player.find_sprite(sprite[0])
            sprite_2 = self.player.find_sprite(sprite[1])

            event_1 = sprite_1.collision(sprite_2)
            event_2 = sprite_2.collision(sprite_1)

            if event_1 == "kill":
                sprites_to_kill.add(sprite_1.sprite_id)
            elif event_1 != None:
                split_collisions.append(event_1)
                sprites_to_kill.add(sprite_1.sprite_id)

            if event_2 == "kill":
                sprites_to_kill.add(sprite_2.sprite_id)
            elif event_2 != None:
                split_collisions.append(event_2)
                sprites_to_kill.add(sprite_2.sprite_id)
                                                      
        for sprite_id in sprites_to_kill:
            
            sprite = self.player.find_sprite(sprite_id)
            sprite.kill()

        return tuple(split_collisions), tuple(sprites_to_kill)

            
            

    



    