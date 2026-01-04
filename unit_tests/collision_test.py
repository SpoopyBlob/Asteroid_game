#pos(1, 2), pos (5, 2) = out_of_bounds no, soft check!, mask check! asteroid normal
#pos(0, 0) pos(64 64) = out_of_bounds no, soft check no, mask check no asteroid normal
#pos(0, 0) pos (63, 64) = out_of bounds no, soft_check !, mask check no asteroid normal
import pygame
from asteroid_game.state import State
from asteroid_game.state import Sprite_Metadata
from asteroid_game.assets import Assets

state = State("spaceship", 1050, 410)
asset = Assets()

#110 x 110 rect
a_t_0 = Sprite_Metadata("1_2_asteroid_0", 1350, 700)
a_t_1 = Sprite_Metadata("2_2_asteroid_1", -120, 0)
a_t_3 = Sprite_Metadata("3_2_asteroid_2", 0, 0)
a_t_4 = Sprite_Metadata("4_2_asteroid_3", 64, 64)
a_t_5 = Sprite_Metadata("5_2_asteroid_4", 1400, 700)

#70 x 70
a_st_1 = Sprite_Metadata("6_1_asteroid_6", 420, 420)
a_st_2 = Sprite_Metadata("7_1_asteroid_6", 500, 500) 
a_st_3 = Sprite_Metadata("8_1_asteroid_6", 870, 560)
a_st_4 = Sprite_Metadata("9_1_asteroid_6", 900, 590)
a_st_5 = Sprite_Metadata("10_1_asteroid_6", 1000, 400)

#150 x 150 rect
a_bt_1 = Sprite_Metadata("11_3_asteroid_6", 1280, 720)
a_bt_2 = Sprite_Metadata("12_3_asteroid_6", 300, 300)
a_bt_2 = Sprite_Metadata("13_3_asteroid_6", 420, -120)










expected_result = ()

