import pygame, sys, random, time
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.init()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((1080, 780))
screen_w, screen_h = pygame.display.get_surface().get_size()

#Images
fighter_image = pygame.image.load("Assets/Ship.png")
fighter_image.set_colorkey((255,255,255))
green_inv = pygame.image.load("Assets/InvaderA2.png").convert_alpha()
red_inv = pygame.image.load("Assets/RedInvader.png").convert_alpha()
yellow_inv = pygame.image.load("Assets/InvaderA1.png").convert_alpha()
background = pygame.image.load("Assets/background.jfif").convert()
background_sc = pygame.transform.scale(background, (screen_w, screen_h))

#Music
pygame.mixer.music.load("Assets/Uranus.mp3")
fire_sound = pygame.mixer.Sound('Assets/shoot.mp3')

clock = pygame.time.Clock()
game_active = True
last_time_spawned = 0
font = pygame.font.SysFont("arial",30)


lives = 3

all_sprites = pygame.sprite.Group()
enemies_sprites = pygame.sprite.Group()
missiles_sprites = pygame.sprite.Group()


y1 = 0
y2 = - screen_h

#Classes
class Fighter(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = fighter_image
        self.rect = self.image.get_rect(midbottom=(screen_w/2, screen_h))


    def update(self):
        if pressed_key[K_RIGHT]:
            self.x = min(self.x + 4, screen_w - fighter_image.get_width())
        if pressed_key[K_LEFT]:
            self.x = max(self.x - 4, 0)

    def draw(self):
        screen.blit(fighter_image, (self.x, self.y))

    def fire(self):
        m = Missile(self.rect.center)
        missiles_sprites.add(m)
        all_sprites.add(m)
        fire_sound.play()

class Missile(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,10))
        pygame.draw.line(self.image,(255,255,255),(2, 10), (2, 0))
        self.rect = self.image.get_rect(midbottom=coordinates)

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

    def draw(self):
        pygame.draw.line(screen, (255,255,255), (self.x + 30, self.y), (self.x + 30, self.y-2))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = red_inv
        self.rect = self.image.get_rect(midbottom=(random.randint(0, 640), 0))

    def update(self):
        self.rect.y += 4


player = Fighter()
all_sprites.add(player)
pygame.mixer.music.play(-1)

while game_active:
    clock.tick(60)

    pressed_key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  #########
        #     # player.fire()

    if time.time() - last_time_spawned > 1:
        e = Enemy()
        enemies_sprites.add(e)
        all_sprites.add(e)
        last_time_spawned = time.time()

        ## Collision detection ##
        collisionEnemMiss = pygame.sprite.groupcollide(enemies_sprites, missiles_sprites, True, True)
        playerCollision = pygame.sprite.spritecollide(player, enemies_sprites, False)
        if playerCollision:
            if lives >=2:
                lives -= 1
            else:
                game_active = False


    ###### rolling bckg ###
    y1 += 2
    y2 += 2
    if y1 == screen_h:
        y1 = -screen_h
    if y2 == screen_h:
        y2 = -screen_h

    ## Rendering
    screen.fill((250, 250, 250))

    screen.blit(background_sc, (0, y1))
    screen.blit(background_sc, (0, y2))

    all_sprites.update()
    all_sprites.draw(screen)


    screen.blit(font.render("Lives: " + str(lives), True, (255, 0, 0)), (50, 20))




        # if enemy.y == screen_h:
        #     if lives > 1:
        #         lives -= 1
        #     else:
        #         game_active = False


    pygame.display.flip()