import pygame, sys, random, time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((1080, 780))
screen_w, screen_h = pygame.display.get_surface().get_size()

#Images
cloudImage = pygame.image.load("cloud.png").convert_alpha()
cloudImage_sc = pygame.transform.scale(cloudImage, (int(0.6*cloudImage.get_width()), int(0.6*cloudImage.get_height())))
avatar_figr = pygame.image.load("avatar.png").convert_alpha()
avatar_figr.set_colorkey((255,255,255))
avatar_figr_umb = pygame.image.load("avatar_umbrella.png").convert_alpha()
avatar_figr_umb.set_colorkey((255,255,255))

clock = pygame.time.Clock()
rain = []
time_since_last_hit = 0

game_active = True


class Raindrops:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = random.randint(8, 20)

	def move(self):
		self.y += self.speed

	def off_screen(self):
		return self.y > screen_h

	def draw(self):
		pygame.draw.circle(screen, (150,150,150), (self.x, self.y), 2)


class Avatar:
	def __init__(self):
		self.x = screen_w/2
		self.y = screen_h - avatar_figr.get_height()

	def hit_by(self, raindrop):
		return pygame.Rect(self.x, self.y, avatar_figr.get_width(), avatar_figr.get_height()).collidepoint((raindrop.x, raindrop.y+2))  #add the radius to the y

	def move(self):
		if pressed_key[K_RIGHT]:
			self.x += 4
			if self.x >= screen_w - 120:
				self.x = screen_w -120
		if pressed_key[K_LEFT]:
			self.x -= 4
			if self.x <= 0:
				self.x = 0

	def draw(self):
		if time.time() - time_since_last_hit > 1:
			screen.blit(avatar_figr, (self.x, self.y))
		else:
			screen.blit(avatar_figr_umb, (self.x, self.y))

class Clouds:
	def __init__(self):
		self.x = 100
		self.y = 20

	def draw(self):
		screen.blit(cloudImage_sc, (self.x, self.y))

	def move(self):
		self.x += 1

	def rain(self):
		# You can use a for in range(10) before append to multiply the raindrops
		rain.append(Raindrops(random.randint(self.x+100, self.x + 500), self.y+200))


player = Avatar()
cloud = Clouds()

# Main Loop
while game_active:
	clock.tick(60)

	pressed_key = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

#Rendering
	screen.fill((250,250,250))

	cloud.move()
	cloud.draw()
	cloud.rain()

	for drop in rain[:]:
		drop.move()

		if drop.off_screen():
			rain.remove(drop)
		elif player.hit_by(drop):
			time_since_last_hit = time.time()
			rain.remove(drop)
		else:
			drop.draw()

	player.move()
	player.draw()