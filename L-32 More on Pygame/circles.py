import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
    pygame.draw.circle(screen,(118,119,12),(60,60),30)
    pygame.draw.circle(screen,(118,119,12),(150,120),30,4)
    pygame.display.flip()