import pygame
from pygame.locals import *

from config import config
from world import world

pygame.init()

# Set up game
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.title)

# Load assets
img_bg = pygame.image.load("./assets/img/sky.png")
img_sun = pygame.image.load("./assets/img/sun.png")

# Draw grid (helps us see where things will go on screen)
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * config.tile_size), (config.width, line * config.tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * config.tile_size, 0), (line * config.tile_size, config.height))

# Game loop
run = True

while run :
  screen.blit(img_bg, (0, 0))
  screen.blit(img_sun, (100, 100))

  world.draw(screen)
  # draw_grid()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
