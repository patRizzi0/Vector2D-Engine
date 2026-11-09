import pygame
from settings import *

def set_barriers(player_1):
    if player_1["y"] >= LIMIT_BOTTOM:
        player_1["y"] = LIMIT_BOTTOM
        player_1["v_y"] = 0.0
    elif player_1["y"] <= 0.0:
        player_1["y"] = 0.0
        player_1["v_y"] = 0.0
    
    if player_1["x"] >= LIMIT_RIGHT:
        player_1["x"] = LIMIT_RIGHT
        player_1["v_x"] = 0.0

    elif player_1["x"] <= 0.0:
        player_1["x"] = 0.0
        player_1["v_x"] = 0.0



    
        