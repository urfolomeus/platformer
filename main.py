import pygame
from pygame.locals import *

import util
from config import config
from world import world

pygame.init()

screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.title)

# Load assets
img_bg = pygame.image.load("./assets/img/sky.png")
img_sun = pygame.image.load("./assets/img/sun.png")

# Game loop
run = True

while run :
  screen.blit(img_bg, (0, 0))
  screen.blit(img_sun, (100, 100))

  world.draw(screen)
  # util.draw_grid(screen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
