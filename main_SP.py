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
green_inv = pygame.image.load("Assets/green.png").convert_alpha()
red_inv = pygame.image.load("Assets/red.png").convert_alpha()
yellow_inv = pygame.image.load("Assets/yellow.png").convert_alpha()
background = pygame.image.load("Assets/background.jfif").convert()
background_sc = pygame.transform.scale(background, (screen_w, screen_h))

#Music
pygame.mixer.music.load("Assets/Uranus.mp3")
fire_sound = pygame.mixer.Sound('Assets/shoot.mp3')

clock = pygame.time.Clock()
game_active = True
last_time_spawned = 0
font = pygame.font.SysFont("arial",30)

missiles = []
enemies = []
lives = 3

y1 = 0
y2 = - screen_h

#Classes
class Fighter:

    def __init__(self):
        self.x = screen_w/2
        self.y = screen_h - 50

    def move(self):
        if pressed_key[K_RIGHT]:
            self.x = min(self.x + 4, screen_w - fighter_image.get_width())
        if pressed_key[K_LEFT]:
            self.x = max(self.x - 4, 0)

    def draw(self):
        screen.blit(fighter_image, (self.x, self.y))

    def fire(self):
        missiles.append(Missile(self.x, self.y))
        fire_sound.play()

class Missile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        self.y -= 10

    def draw(self):
        pygame.draw.line(screen, (255,255,255), (self.x + 30, self.y), (self.x + 30, self.y-2))

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 640)
        self.y = -40

    def move(self):
        self.y += 10

    def draw(self):
        screen.blit(green_inv, (self.x,self.y))

    def hitby(self, missile):
        return pygame.Rect(self.x, self.y, green_inv.get_width(), green_inv.get_height()).clipline(
            (missile.x + 30, missile.y + 30), (missile.x + 30, missile.y - 5))


player = Fighter()
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
        enemies.append(Enemy())
        last_time_spawned = time.time()

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
    player.draw()
    player.move()

    screen.blit(font.render("Lives: " + str(lives), True, (255, 0, 0)), (50, 20))

    for m in missiles:
        m.draw()
        m.move()

    for enemy in enemies:
        enemy.draw()
        enemy.move()
        if enemy.y == screen_h:
            if lives > 1:
                lives -= 1
            else:
                game_active = False


    k = 0
    while k < len(enemies):
        i = 0
        while i < len(missiles):
            if enemies[k].hitby(missiles[i]):
                del enemies[k]
                del missiles[i]
                k -= 1
                break
            i += 1
        k += 1

    pygame.display.flip()