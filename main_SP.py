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
pink_inv1 = pygame.image.load("Assets/enemy1_1.png").convert_alpha()
pink_inv2 = pygame.image.load("Assets/enemy1_2.png").convert_alpha()
spr_explo = pygame.image.load("Assets/Explosions/regularExplosion00.png").convert_alpha()
background = pygame.image.load("Assets/background.jfif").convert()
background_sc = pygame.transform.scale(background, (screen_w, screen_h))
spritesheet = pygame.image.load("Assets/pixel_character_spritesheets_48x48/pixel_character_pale_yellow.png").convert_alpha()


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

moving_inv = [pink_inv1, pink_inv2]
Explosions = []

# Load Images in a list for explosion animations
for i in range(9):
    filename = 'Assets/Explosions/regularExplosion00.png'.format(i)
    explosion_image = pygame.image.load(filename).convert_alpha()
    Explosions.append(explosion_image)

y1 = 0
y2 = - screen_h

#Classes
class Fighter(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.subsurface((0,192,48,48 ))
        self.rect = self.image.get_rect(midbottom=(screen_w/2, screen_h))


    def update(self):
        if pressed_key[K_RIGHT]:
            self.rect.x = min(self.rect.x + 4, screen_w - fighter_image.get_width())
        if pressed_key[K_LEFT]:
            self.rect.x = max(self.rect.x - 4, 0)

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = moving_inv[0]
        self.rect = self.image.get_rect(midbottom=(random.randint(0, 640), 0))
        self.index = 0
        # self.current_frame = 0
        self.time_since_last_pose = 10
        self.angle = 0



    def update(self):
        self.rect.y += 4

        old_center = self.rect.center
        self.angle = (self.angle + 2)%360

        # self.current_frame += 1
        # if self.current_frame >= self.nr_frames_between:
        if time.time() - self.time_since_last_pose > 0.2:
            self.index = (self.index + 1)%len(moving_inv)
            self.image = moving_inv[self.index]
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=old_center)
            self.time_since_last_pose = time.time()


class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Explosions[0]
        self.rect = self.image.get_rect(center=coord)
        self.old_center = self.rect.center
        self.time_since_last_image = 0
        self.index = 0

    def update(self):

        if time.time() - self.time_since_last_image > 0.1:
            self.kill()
        else:
            self.index = (self.index + 1) % len(Explosions)
            self.image = Explosions[self.index]








player = Fighter()
all_sprites.add(player)
pygame.mixer.music.play(-1)

while game_active:
    clock.tick(60)

    pressed_key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  #########
            player.fire()

    if time.time() - last_time_spawned > 1:
        e = Enemy()
        enemies_sprites.add(e)
        all_sprites.add(e)
        last_time_spawned = time.time()

        ## Collision detection ##
        collisionEnemMiss = pygame.sprite.groupcollide(enemies_sprites, missiles_sprites, True, True)
        for i in collisionEnemMiss:
            e = Explosions(i.rect.center)
            all_sprites.add(e)

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