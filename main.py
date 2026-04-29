# imports
import pygame
from pygame import mixer
from Tile import Tile

screen = pygame.display.set_mode((900, 600))

color = (0,0,50)
test_tile = Tile(50,50,50,50,color)
while True:
    test_tile.display(screen)