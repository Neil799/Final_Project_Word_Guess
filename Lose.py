import pygame



class Lose:
    
    def __init__(self, name):
        self.name = name
    def display(self, screen, answer):
        screen.fill("cadetblue3")
        font = pygame.font.SysFont('felixtitling', 48)
        font2 = pygame.font.SysFont('felixtitling', 30)

        letter_surface = font.render("You lost!", True, "white")
        screen.blit(letter_surface, (95, 50))

        answer_surface = font2.render(f"The word was {answer}", True, "white")
        screen.blit(answer_surface, (65,240))
