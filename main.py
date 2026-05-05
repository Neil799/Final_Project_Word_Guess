# note to self: find a way to find the center of each box

# imports
import pygame
import random
from pygame import mixer
from Tile import Tile
# from Board import Board
import time
pygame.init()


SCREEN_WIDTH = 457
SCREEN_HEIGHT = 554
FONT_COLOR = (0,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

empty_box_color = (194,197,204)
    
font = pygame.font.SysFont('Felix Titling', 50)

def main():
    column = 0
    feedback = ""
    words = ["slate", "drink", "jumpy","emcee","snake","cobra", "glass", "trait", "water", "bells", "preps", "pants", "shoes", "grade"]
    target_word = random.choice(words)
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
                    word += letter
                    letter_surface = font.render(letter, True, FONT_COLOR)
                    screen.blit(letter_surface, (LETTER_X_POS, LETTER_Y_POS))
                    LETTER_X_POS+=85
                    if len(word) == 5:
                        for i in range(5):
                            if word[i] == target_word[i]:
                                letter_surface = font.render(word[i], True, "Green")
                                screen.blit(letter_surface, (40+i*85, 20+column*90))
                            elif word[i] in target_word:
                                letter_surface = font.render(word[i], True, "Yellow")
                                screen.blit(letter_surface, (40+i*85, 20+column*90))
                            else:
                                letter_surface = font.render(word[i], True, "Grey")
                                screen.blit(letter_surface, (40+i*85, 20+column*90))
                        # note: make it enter so change vvvv
                        if word == target_word:
                            print("you won!")
                            
                        elif column != 5:
                            column +=1
                        else:
                            print("You lost, word was " + target_word)
                    # elif event.key == pygame.K_BACKSPACE:
                        
                        

                        print(feedback)
                        LETTER_X_POS = 40
                        LETTER_Y_POS += 90
                        word = ""
                        feedback = ""

                    # note add most of the above stuff into board class
            if event.type == pygame.QUIT:
                pygame.quit()
            
if __name__ == "__main__":
    main()
    pygame.quit()