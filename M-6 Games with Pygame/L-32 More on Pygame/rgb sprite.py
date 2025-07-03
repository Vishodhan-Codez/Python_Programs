import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600,600))
tre = True
def randcolor():
    return random.choices(range(256),k=3)
while tre :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    pygame.draw.rect(screen,randcolor(),pygame.Rect(250,250,100,50))
    pygame.display.update()
