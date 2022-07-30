import pygame
from pygame.locals import *

pygame.init()

SCREEN_OPTS = {
  "width": 1000,
  "height": 1000,
}

screen = pygame.display.set_mode((SCREEN_OPTS["width"], SCREEN_OPTS["height"]))
pygame.display.set_caption("Platformer")

run = True

while run :

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()
