import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
done = True
while done :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    pygame.draw.rect(screen,(119,200,178),pygame.Rect(30,30,40,40))
    pygame.display.flip()
