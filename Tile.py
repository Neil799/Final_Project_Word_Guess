import pygame

class Tile:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rect = pygame.Rect(x, y, width, height)
    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    
