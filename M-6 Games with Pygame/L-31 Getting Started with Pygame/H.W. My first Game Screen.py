import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game screen")
c = pygame.image.load("1.png").convert_alpha()
c = pygame.transform.scale(c,(150,150))
while not False :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    screen.fill((58,58,58))
    screen.blit(c,(150,150))
    pygame.display.flip()