# note to self: find a way to find the center of each box

# imports
import pygame
from pygame import mixer
from Tile import Tile
from Board import Board
pygame.init()


SCREEN_WIDTH = 457
SCREEN_HEIGHT = 554
FONT_COLOR = (0,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

empty_box_color = (194,197,204)
    
font = pygame.font.SysFont('Felix Titling', 50)

def main():
    word = ""
    LETTER_X_POS = 40
    LETTER_Y_POS = 20
    letter = ""
    running = True
    
    # box = Tile(14,17,77,77,empty_box_color)
    grid = pygame.image.load('blankgrid.jpg').convert_alpha()
    screen.blit(grid, (0, 0))
    while running:
        
        
        # box.display(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    letter = event.unicode
                    print(letter)
                    word += letter
                    letter_surface = font.render(letter, True, FONT_COLOR)
                    screen.blit(letter_surface, (LETTER_X_POS, LETTER_Y_POS))
                    LETTER_X_POS+=85
                    if len(word) == 5:
                        print("hooray! "+word)
                        LETTER_X_POS = 40
                        LETTER_Y_POS += 90
                        word = ""

                    # note add most of the above stuff into board class
            if event.type == pygame.QUIT:
                pygame.quit()
            
if __name__ == "__main__":
    main()
    pygame.quit()