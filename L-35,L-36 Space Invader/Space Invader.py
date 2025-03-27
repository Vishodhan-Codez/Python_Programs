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
got = psy-20 #game over threshold

pygame.init()
screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("")
pygame.display.set_icon(icon)
bg = pygame.image.load("")
p_img = pygame.image.load("")
e_img = pygame.image.load("")
b_img = pygame.image.load("")

font = pygame.font.Font("freetransbold.ttf",32)
overFont = pygame.font.Font("freetransbold.ttf",64)

enemy = [
    {
        "x":random.randint(0,sw-64),
        "y":random.randint(50,150),
        "dx":esx
    } for _ in range(6)
]
bx = 0
by = psy
bs = "ready"

px,py = psx,psy
px_c = 0

score = 0 

def showscore():
    score1 = font.render(f"Score:{score}",True,(255,255,255))
    screen.blit(score1,10,10)
def over() :
    over1 = font.render(f"Game Over !",True,(255,255,255))
    screen.blit(over1,200,250)
def dp() :
    screen.blit(p_img,(px,py))
def ep(enemy) :
    screen.blit(e_img,enemy["x"],enemy["y"])
def bull() :
    screen.blit(b_img,(bx+10,by+16))
def coll_detect(enemy) :
    return math.hypot(enemy["x"]-bx,enemy["y"]-by) < collision
