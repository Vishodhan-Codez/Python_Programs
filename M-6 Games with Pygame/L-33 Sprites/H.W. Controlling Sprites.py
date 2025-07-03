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

sprite1_event = pygame.USEREVENT + 1
bg_event = pygame.USEREVENT + 2
bgcolor = green

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

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
            pygame.event.post(pygame.event.Event(sprite1_event))
            pygame.event.post(pygame.event.Event(bg_event))

    def change_color(self):
        self.image.fill(random.choice([white, yellow, orange]))

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = 5
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 400:
            self.rect.y += self.speed
 
def change_bg():
    global bgcolor
    bgcolor = random.choice([blue, black, red])
all_sprites = pygame.sprite.Group()
bouncing_sprite = Sprite(red, 50, 40)
bouncing_sprite.rect.x = random.randint(0, 450)
bouncing_sprite.rect.y = random.randint(0, 350)
player_sprite = Player(white, 50, 50)
player_sprite.rect.x = 200
player_sprite.rect.y = 200
all_sprites.add(bouncing_sprite)
all_sprites.add(player_sprite)
screen = pygame.display.set_mode((500, 400))
screen.fill(bgcolor)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == sprite1_event:
            bouncing_sprite.change_color()
        elif event.type == bg_event:
            change_bg()

    keys = pygame.key.get_pressed()
    player_sprite.move(keys)

    all_sprites.update()
    screen.fill(bgcolor)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
