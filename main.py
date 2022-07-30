import pygame
from pygame.locals import *

pygame.init()

# Set up game
SCREEN_OPTS = {
  "width": 1000,
  "height": 1000,
}
TILE_SIZE = 200

screen = pygame.display.set_mode((SCREEN_OPTS["width"], SCREEN_OPTS["height"]))
pygame.display.set_caption("Platformer")

# Load assets
img_bg = pygame.image.load("./assets/img/sky.png")
img_sun = pygame.image.load("./assets/img/sun.png")

# Draw grid (helps us see where things will go on screen)
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * TILE_SIZE), (SCREEN_OPTS["width"], line * TILE_SIZE))
		pygame.draw.line(screen, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, SCREEN_OPTS["height"]))

# Game loop
run = True

while run :
  screen.blit(img_bg, (0, 0))
  screen.blit(img_sun, (100, 100))

  draw_grid()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
