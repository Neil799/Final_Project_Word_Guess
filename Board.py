import pygame
# import random
from Tile import Tile



class Board:

     def __init__(self, name):
        self.name = name
     def determine_correctness(self, letter, answer_letter, answer):
          if letter.lower() == answer_letter:
            return "Green"
            

          elif letter.lower() in answer:
            return "Yellow"

          else:
            return "Grey"
  
     def redraw_letters(self, screen, letter, color, font, x_pos, y_pos):
          letter_surface = font.render(letter, True, color)
          screen.blit(letter_surface, (x_pos, y_pos))
     def redraw_boxes(self, screen, letter, color, x_pos, y_pos):
          redrawed_tile = Tile(x_pos, y_pos, 73, 73, color)
          redrawed_tile.display(screen)
          
#     print("Board!")
#     def word_chooser(self):
#         words = ["sleep", "drink", "basin"]
#         secret_word = random.randint(words)
#         print(secret_word)
#     # note: this class will store guesses and determine guess correctness