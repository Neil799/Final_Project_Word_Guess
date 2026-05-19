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

          if letter not in answer:
              return Grey

          total_letters = answer.count(letter)
          letter_used = 0
          for j in range(i):
              if guess[j].lower() != letter:
                  continue
              if guess[j].lower() == answer[j]:
                  letter_used += 1
              elif letter_used < total_letters:
                  letter_used += 1

          if letter_used < total_letters:
              return Yellow
          return Grey
  
     def redraw_letters(self, screen, letter, color, font, x_pos, y_pos):
          letter_surface = font.render(letter, True, color)
          screen.blit(letter_surface, (x_pos, y_pos))
     def redraw_boxes(self, screen, letter, color, x_pos, y_pos):
          redrawed_tile = Tile(x_pos, y_pos, 73, 73, color)
          redrawed_tile.display(screen)
   