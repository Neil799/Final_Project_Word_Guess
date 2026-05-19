import pygame
# import random
from Tile import Tile

Green = (108,169,101)
Yellow = (200,182,83)
Grey = (120,124,127)

class Board:

     def __init__(self, name):
        self.name = name
     def determine_correctness(self, i, answer, guess):
          letter = guess[i].lower()
          if letter == answer[i]:
              return Green
            # ^^ automaticaly checks if the letter = same positoin as letter in answer 
          else:
            available_letters = [] #this will turn into the available letters in teh answer
            for j in range(5):
                if guess[j].lower() != answer[j]:
                    available_letters.append(answer[j]) #this is to make sure that we dont add letters taht are green in here

            for j in range(i): #j in range(i) so it looks at every lettter at every index before i
                if guess[j].lower() != answer[j] and guess[j].lower() in available_letters:
                    available_letters.remove(guess[j].lower())
                    # removes any earlier guess letters that arent green from the answer letters so that we dont acidentally count one letter twice and mess up yellow detection

            if letter in available_letters:
                return Yellow
            return Grey
    
     def redraw_letters(self, screen, letter, color, font, x_pos, y_pos):
          letter_surface = font.render(letter, True, color)
          screen.blit(letter_surface, (x_pos, y_pos))
     def redraw_boxes(self, screen, letter, color, x_pos, y_pos):
          redrawed_tile = Tile(x_pos, y_pos, 73, 73, color)
          redrawed_tile.display(screen)
   