import pygame
pygame.init()
scr = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Game Screen")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.fill((255, 255, 255))
    pygame.draw.rect(scr,(119, 200, 178), pygame.Rect(220, 190, 250, 100))
    txt = pygame.font.Font(None, 36).render("Hello, Pygame!", True, (0, 0, 0)) #got from online
    scr.blit(txt, (250, 220))
    pygame.display.flip()
