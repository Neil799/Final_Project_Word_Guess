import pygame

Green = (108,169,101)


class Win:
    
    def __init__(self, name):
        self.name = name
    def display(self, screen, answer, num_guesses):
        screen.fill("pink")
        font = pygame.font.SysFont('felixtitling', 48)
        font2 = pygame.font.SysFont('felixtitling', 30)

        letter_surface = font.render("You won!", True, "orange")
        screen.blit(letter_surface, (95, 50))
        if num_guesses == 1:
            letter_surface = font2.render(f"It took you {num_guesses} guess!", True, "orange")
        else:
            letter_surface = font2.render(f"It took you {num_guesses} guesses!", True, "orange")
        screen.blit(letter_surface, (35, 100))

        answer_surface = font.render(answer, True, Green)
        screen.blit(answer_surface, (95,240))
