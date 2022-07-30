import pygame
from pygame.locals import *

pygame.init()

# Set up game
SCREEN_OPTS = {
  "width": 1000,
  "height": 1000,
}

screen = pygame.display.set_mode((SCREEN_OPTS["width"], SCREEN_OPTS["height"]))
pygame.display.set_caption("Platformer")

# Load assets
img_bg = pygame.image.load("./assets/img/sky.png")
img_sun = pygame.image.load("./assets/img/sun.png")

# Game loop
run = True

while run :
  screen.blit(img_bg, (0, 0))
  screen.blit(img_sun, (100, 100))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
