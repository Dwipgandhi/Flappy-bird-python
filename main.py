import random
import sys
import pygame
from pygame.locals import *

fps = 32
screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width,screen_height))
ground_y = screen_height*0.8
game_images = {}
game_sounds = {}
player = 'gallery/images/bird-midflap.png'
background = 'gallery/images/background.png'
pipe = 'gallery/images/pipe.png'
title = 'gallery/images/title.png'
