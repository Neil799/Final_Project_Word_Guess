# note to self: find a way to find the center of each box

# imports
import random
import time
import pygame
from pygame import mixer
from Tile import Tile
from Board import Board
from Win import Win
from Lose import Lose
pygame.init()
mixer.init()
# mixer.music.play(), mixer.music.load("./sounds/bounce.mp3"), mixer.music.set_volume(0.7)

guess_sound = mixer.Sound("./sounds/guess_sound.wav")
win_sound = mixer.Sound("./sounds/win_sound.mp3")
lose_sound = mixer.Sound("./sounds/sad_sound.wav")
win_sound.set_volume(0.7)
guess_sound.set_volume(0.7)
lose_sound.set_volume(0.7)

SCREEN_WIDTH = 457
SCREEN_HEIGHT = 547
FONT_COLOR = (0,0,0)

empty_box_color = (194,197,204)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont('felixtitling', 48)


file = open("validword.txt", "r")
valid_words = file.read()
file.close()
valid_words = valid_words.split("\n")

file = open("answerwords.txt", "r")
answer_words = file.read()
file.close()
answer_words = answer_words.split("\n")

def draw_tiled_grid(screen):
    for z in range(6):
        for k in range(5):
            box = Tile((87.8*k)+15,(87.8*z)+18,73,73,empty_box_color)
            box.display(screen)
def main():
    column = 0
    target_word = random.choice(answer_words)
    # print(target_word)
    word = ""
    LETTER_X_POS = 40
    LETTER_Y_POS = 20
    letter = ""
    colors_list = []
    line_skip_counter = 0
    num_guesses = 0
    letters_list = []
    running = True
    done = False
    wordle_board = Board("Wordle_Board")
    win_screen = Win("Win_Screen")
    lose_screen = Lose("Lose_Screen")
    # grid = pygame.image.load('blankgrid.jpg').convert_alpha()
    # screen.blit(grid, (0, 0))
    # screen.fill(WHITE)
    draw_tiled_grid(screen)

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
                            letters_list.append(letter)
                            colors_list.append("black")
                            letter_surface = font.render(letter, True, FONT_COLOR)
                            screen.blit(letter_surface, (LETTER_X_POS, LETTER_Y_POS))
                            LETTER_X_POS+=87.8
                            
                            

                            # elif event.key == pygame.K_BACKSPACE:
                    

                    elif event.key == pygame.K_RETURN:
                        
                        if len(word) == 5:
                                
                            if word.lower() in valid_words:
                                guess_sound.play()
                                num_guesses+=1  
                                for x in range(5):
                                        del letters_list[-1]
                                        del colors_list[-1]

                                for i in range(5):
                                    
                                    color = wordle_board.determine_correctness(i, target_word, word)
                                    
                                    colored_tile = Tile(15+i*87.8,18+column*87.8,73,73,color)
                                    colored_tile.display(screen)
                                    letter_surface = font.render(word[i], True, "white")
                                    screen.blit(letter_surface, (40+i*87.8, 20+column*87.8))
                                    colors_list.append(color)
                                    letters_list.append(word[i])
                                if word.lower() == target_word:
                                    print("you won!")
                                    pygame.display.flip() 
                                    pygame.time.delay(2000)
                                    win_sound.play()
                                    done = True
                                    win_screen.display(screen, target_word, num_guesses)
                                elif column != 5:
                                    column +=1
                                else:

                                    print("You lost, word was " + target_word)
                                    pygame.display.flip()
                                    pygame.time.delay(2000)
                                    lose_sound.play()
                                    done = True
                                    lose_screen.display(screen, target_word)
                        
                                print("enter key")
                                LETTER_X_POS = 40
                                LETTER_Y_POS += 87.8
                                word = ""
                            else:
                                print("invalid word")
                        # note add most of the above stuff into board class
                    elif event.key == pygame.K_BACKSPACE:
                        if len(word) != 0:
                            del letters_list[-1]
                            del colors_list[-1]
                            word = word[:-1]
                            # word = ""
                            # screen.blit(grid, (0,0))
                            LETTER_X_POS = 15
                            LETTER_Y_POS = 18
                            line_skip_counter = 0
                            # screen.fill(WHITE)
                            draw_tiled_grid(screen)
                            for s in range(num_guesses*5):
                                wordle_board.redraw_boxes(screen, letters_list[s], colors_list[s], LETTER_X_POS, LETTER_Y_POS)
                                LETTER_X_POS += 87.8
                                line_skip_counter+=1
                                if line_skip_counter == 5:
                                    LETTER_Y_POS += 87.8
                                    line_skip_counter = 0
                                    LETTER_X_POS = 15
                            LETTER_X_POS = 40
                            LETTER_Y_POS = 20
                            for j in range(len(letters_list)): 
                                if j < num_guesses*5:
                                    letter_color = WHITE
                                else:
                                    letter_color = BLACK
                                wordle_board.redraw_letters(screen, letters_list[j], letter_color, font, LETTER_X_POS, LETTER_Y_POS)
                                LETTER_X_POS += 87.8
                                line_skip_counter+=1
                                if line_skip_counter == 5:
                                    LETTER_Y_POS += 87.8
                                    line_skip_counter = 0
                                    LETTER_X_POS = 40
                            
                                
                                

                            
                
            
if __name__ == "__main__":
    main()
    pygame.quit()