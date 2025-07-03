import math
import pygame
import random
sw = 800
sh = 400
psx = 370
psy = 220
esx = 2
esy = 20
collision = 28
bull_speed = 10 
got = psy - 20  

pygame.init()
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Space Invader")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("background.png")
p_img = pygame.image.load("player.png")
e_img = pygame.image.load("enemy.png")
b_img = pygame.image.load("bullet.png")

font = pygame.font.Font("freesansbold.ttf", 32)
overFont = pygame.font.Font("freesansbold.ttf", 64)

pygame.mixer.music.load("background.mp3")  
pygame.mixer.music.play(-1) 
shoot_sound = pygame.mixer.Sound("shoot.mp3")  
explosion_sound = pygame.mixer.Sound("explosion.mp3")  

# Enemy list
enemy = [
    {
        "x": random.randint(0, sw - 64),
        "y": random.randint(50, 150),
        "dx": esx
    } for _ in range(6)
]

bx = 0
by = psy
bs = "ready"  

px, py = psx, psy
px_c = 0  

score = 0  

# Functions
def showscore():
    score1 = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score1, (10, 10))

def over():
    over1 = overFont.render("Game Over!", True, (255, 255, 255))
    screen.blit(over1, (200, 250))

def dp():
    screen.blit(p_img, (px, py))

def ep(enemy):
    screen.blit(e_img, (enemy["x"], enemy["y"]))

def bull():
    screen.blit(b_img, (bx + 10, by + 16))

def coll_detect(enemy):
    return math.hypot(enemy["x"] - bx, enemy["y"] - by) < collision

# Game loop
running = True
while running:
    screen.blit(bg, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px_c = -5
            if event.key == pygame.K_RIGHT:
                px_c = 5
            if event.key == pygame.K_SPACE and bs == "ready":
                shoot_sound.play()  
                bx = px + 16 
                bs = "fire"

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                px_c = 0

    px = max(0, min(px + px_c, sw - 64))

    for i in enemy:
        if i["y"] >= got and abs(i["x"] - px) < collision:
            for e in enemy:
                e["y"] = 2000
            over()
            pygame.display.update()
            pygame.time.wait(2000) 
            running = False
            break

        i["x"] += i["dx"]
        if i["x"] <= 0 or i["x"] >= sw - 64:
            i["dx"] *= -1
            i["y"] += esy

        if coll_detect(i):
            explosion_sound.play()  
            by = psy
            bs = "ready"
            score += 1
            i["x"] = random.randint(0, sw - 64)
            i["y"] = random.randint(50, 150)

        ep(i)

    if bs == "fire":
        bull()
        by -= bull_speed
        if by <= 0:
            bs = "ready"
            by = psy

    showscore()
    dp()
    pygame.display.update()
