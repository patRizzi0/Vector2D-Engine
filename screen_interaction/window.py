import pygame

def create_window(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))