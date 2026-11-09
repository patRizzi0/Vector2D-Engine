import pygame
from screen_interaction.exit import event_quit
from screen_interaction.window import create_window
from square.square_init import draw_rect
from player import player
from window_barrier.barriers import set_barriers
from input.directions_wasd import *


from settings import *
#Window init
window = create_window(WIDTH, HEIGHT)

#spawn_point
player_1 = player(300.0, 150.0)

# s = s0 + v * dt
def mru_1D(player_1,dt):
    player_1["x"] += player_1["v_x"] * dt

def mru_2D(player_1,dt):
    player_1["x"] += player_1["v_x"] * dt
    player_1["y"] += player_1["v_y"] * dt 

def mrua_2D(player_1,dt):
    player_1["v_y"] += g * dt
    mru_2D(player_1,dt)



pygame.init()
time = pygame.time.Clock()


toccato = False
running = True
while running:
    running = input_handler(player_1)

    window.fill((0, 0, 0))

    dt_ms = time.tick(FPS)
    dt = dt_ms / 1000

    
    #mru_1D(player_1,dt) #Moto Rettilineo Uniforme
    #mru_2D(player_1,dt)
    mrua_2D(player_1,dt)
    
    set_barriers(player_1)

    draw_rect(window,player_1["x"],player_1["y"])
    

    pygame.display.flip()

pygame.quit()