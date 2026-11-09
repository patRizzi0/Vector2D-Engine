import pygame
from settings import *


#Color Rectangle
RED = (100,0,0)
WIDTH_RECT = 120
HEIGHT_RECT = 80

#Position
x = 400.0
y = 250.0

def draw_rect(window,x,y):
    pygame.draw.rect(window, RED,(int(x),int(y), WIDTH_RECT, HEIGHT_RECT))






