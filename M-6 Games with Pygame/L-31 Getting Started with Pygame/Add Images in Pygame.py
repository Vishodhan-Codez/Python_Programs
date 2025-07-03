import pygame
pygame.init()
s = pygame.display.set_mode((500,500))
c = pygame.image.load("1.png").convert_alpha()
c = pygame.transform.scale(c,(200,200))
while not False :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
    s.fill((82,134,186))
    s.blit(c,(200,200))
    pygame.display.flip()