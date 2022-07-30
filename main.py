import pygame
from pygame.locals import *

import util
from config import config
from player import Player
from world import world

PLAYER_START_X = 100

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.title)

# Load assets
img_bg = pygame.image.load("./assets/img/sky.png")
img_sun = pygame.image.load("./assets/img/sun.png")

# Create objects
player = Player(config.player_start_x, config.player_start_y)

# Game loop
run = True

while run :
  clock.tick(config.fps)

  screen.blit(img_bg, (0, 0))
  screen.blit(img_sun, (100, 100))

  world.draw(screen)
  # util.draw_grid(screen)
  player.update(screen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
