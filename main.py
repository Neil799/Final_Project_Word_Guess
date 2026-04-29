# imports
import pygame
from pygame import mixer
from Tile import Tile
from Board import Board

screen = pygame.display.set_mode((900, 600))

empty_box_color = (194,197,204)
    

def main():
    running = True
    
    box = Tile(250,50,60,60,empty_box_color)
    while running:
        
        
        box.display(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False
    
if __name__ == "__main__":
    main()
    pygame.quit()