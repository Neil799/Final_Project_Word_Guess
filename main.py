# note to self: find a way to find the center of each box

# imports
import pygame
import random
from pygame import mixer
from Tile import Tile
from Board import Board
import time
pygame.init()


SCREEN_WIDTH = 457
SCREEN_HEIGHT = 547
FONT_COLOR = (0,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# empty_box_color = (194,197,204)
    
font = pygame.font.SysFont('felixtitling', 48)


file = open("validword.txt", "r")
valid_words = file.read()
file.close()
valid_words = valid_words.split("\n")

def main():
    column = 0
    feedback = ""
    words = ["slate", "drink", "jumpy","emcee","snake","cobra", "glass", "trait", "water", "bells", "preps", "pants", "shoes", "grade"]
    target_word = random.choice(valid_words)
    word = ""
    LETTER_X_POS = 40
    LETTER_Y_POS = 20
    letter = ""
    colors_list = []
    line_skip_counter = 0
    letters_list = []
    running = True
    done = False
    # box = Tile(14,17,77,77,empty_box_color)
    wordle_board = Board("Wordle_Board")
    grid = pygame.image.load('blankgrid.jpg').convert_alpha()
    screen.blit(grid, (0, 0))
    while running:
        
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if done == False:
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        if len(word) != 5:
                            letter = event.unicode
                            letter = letter.upper()
                            word += letter
                            print(word)
                            letter_surface = font.render(letter, True, FONT_COLOR)
                            screen.blit(letter_surface, (LETTER_X_POS, LETTER_Y_POS))
                            LETTER_X_POS+=85
                            

                            # elif event.key == pygame.K_BACKSPACE:
                    

                    elif event.key == pygame.K_RETURN:
                        
                        if len(word) == 5:
                                
                            if word.lower() in valid_words:
                                    
                                for i in range(5):
                                    color = wordle_board.determine_correctness(word[i], target_word[i], target_word)
                                    letter_surface = font.render(word[i], True, color)
                                    screen.blit(letter_surface, (40+i*85, 20+column*90))
                                    colors_list.append(color)
                                    letters_list.append(word[i])
                                # note: make it enter so change vvvv
                                
                                if word.lower() == target_word:
                                    print("you won!")
                                    done = True
                                elif column != 5:
                                    column +=1
                                else:
                                    print("You lost, word was " + target_word)
                                    done = True
                        
                                print("enter key")
                                LETTER_X_POS = 40
                                LETTER_Y_POS += 90
                                word = ""
                            else:
                                print("invalid word")
                        # note add most of the above stuff into board class
                    elif event.key == pygame.K_BACKSPACE:
                        if len(word) != 0:
                            # word = word[:-1]
                            word = ""
                            screen.blit(grid, (0,0))
                            LETTER_X_POS = 40
                            LETTER_Y_POS = 20
                            for j in range(len(letters_list)):
                                wordle_board.redraw(screen, letters_list[j], colors_list[j], font, LETTER_X_POS, LETTER_Y_POS)
                                LETTER_X_POS += 85
                                line_skip_counter+=1
                                if line_skip_counter == 5:
                                    LETTER_Y_POS += 90
                                    line_skip_counter = 0
                                    LETTER_X_POS = 40
                            
                                
                                

                            
                
            
if __name__ == "__main__":
    main()
    pygame.quit()