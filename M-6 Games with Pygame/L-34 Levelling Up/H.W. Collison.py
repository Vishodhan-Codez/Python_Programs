import pygame, random

pygame.init()
clock = pygame.time.Clock()
blue = pygame.Color("Blue")
white = pygame.Color("White")
red = pygame.Color("Red")
black = pygame.Color("Black")
orange = pygame.Color("Orange")
yellow = pygame.Color("Yellow")
green = pygame.Color("Green")
sprite_event = pygame.USEREVENT + 1
bg_event = pygame.USEREVENT + 2
bgcolor = green

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]

    def update(self):
        self.rect.move_ip(self.velocity)
        bounced = False
        
        if self.rect.left <= 0 or self.rect.right >= 500:
            bounced = True
            self.velocity[0] = -self.velocity[0]
        
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            bounced = True
            self.velocity[1] = -self.velocity[1]

        if bounced:
            pygame.event.post(pygame.event.Event(sprite_event))
            pygame.event.post(pygame.event.Event(bg_event))

    def change_color(self):
        self.image.fill(random.choice([white, yellow, orange]))

def change_bg():
    global bgcolor
    bgcolor = random.choice([blue, black, red])
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(red, 50, 50)
sprite1.rect.x = random.randint(0, 450)
sprite1.rect.y = random.randint(0, 350)

sprite2 = Sprite(blue, 50, 50)
sprite2.rect.x = random.randint(0, 450)
sprite2.rect.y = random.randint(0, 350)

all_sprites.add(sprite1, sprite2)
screen = pygame.display.set_mode((500, 400))
screen.fill(bgcolor)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == sprite_event:
            sprite1.change_color()
            sprite2.change_color()
        elif event.type == bg_event:
            change_bg()

    all_sprites.update()
    screen.fill(bgcolor)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
