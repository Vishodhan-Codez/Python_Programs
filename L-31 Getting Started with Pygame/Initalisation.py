import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("New Game")
s = False
while not s :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
    pygame.display.flip()