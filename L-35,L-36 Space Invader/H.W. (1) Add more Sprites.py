# this took a lot of time sir, i saw a video and did it

import pygame, random
pygame.init()

W = 800
H = 600
scr = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sprite Game")
WHT, BLU, RED, BLK = (255, 255, 255), (50, 150, 250), (250, 50, 50), (0, 0, 0)
p_size, p_spd = 50, 5
p = pygame.Rect(W//2, H-100, p_size, p_size)

e_size = 40
enemies = [pygame.Rect(random.randint(0, W-e_size), random.randint(0, H-200), e_size, e_size) for _ in range(7)]
score, font = 0, pygame.font.Font(None, 36)

def game_over():
    scr.fill(WHT)
    scr.blit(font.render(f"Game Over! Score: {score}", True, BLK), (W//2 - 100, H//2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    exit()

run, clk = True, pygame.time.Clock()
while run:
    scr.fill(WHT)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] : 
        p.x -= p_spd
    if keys[pygame.K_RIGHT] : 
        p.x += p_spd
    if keys[pygame.K_UP]: 
        p.y -= p_spd
    if keys[pygame.K_DOWN]: 
        p.y += p_spd

    if p.x <= 0 or p.x >= W - p_size :
        game_over()
    elif p.y <= 0 or p.y >= H - p_size :
        game_over()

    for e in enemies:
        if p.colliderect(e):
            score += 1
            e.x, e.y = random.randint(0, W - e_size), random.randint(0, H - 200)
            p_spd += 0.5
    pygame.draw.rect(scr, BLU, p)
    for e in enemies:
        pygame.draw.rect(scr, RED, e)
    scr.blit(font.render(f"Score: {score}", True, BLK), (10, 10))
    
    pygame.display.flip()
    clk.tick(30)

pygame.quit()


