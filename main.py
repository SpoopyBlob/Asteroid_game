import pygame
from asteroid_game.state import State
from asteroid_game.render import Render
from asteroid_game.logic import Logic
from asteroid_game.collisions import Collision


#temp
from asteroid_game.state import Sprite_Metadata

def main():
    dt = 0
    clock = pygame.time.Clock()
    render = Render()

    logic = Logic()
    player_date = logic.init_player()
    
    state = State(player_date.id, player_date)
    collision = Collision()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        data = state.get_state()
        data = logic.update(data, dt)
        data = collision.update(data)
        state.set_state(data)
        
        render.draw(data)

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

