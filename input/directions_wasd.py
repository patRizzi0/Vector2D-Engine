import pygame
from movements.x_y import *
from screen_interaction.exit import *


def input_handler(player_1):
    running = True
    for event in pygame.event.get():
        if event_quit(event):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1["v_y"] = -300
            if event.key == pygame.K_a:
                player_1["v_x"] = -250
            if event.key == pygame.K_s:
                player_1["v_y"] = 300
            if event.key == pygame.K_d:
                player_1["v_x"] = 250
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                player_1["v_x"] = 0.0
            if event.key in (pygame.K_w, pygame.K_s):
                player_1["v_y"] = 0.0
    return running
