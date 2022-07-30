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

class World:
  def __init__(self, data):
    self.tile_list = []

    # load images
    img_dirt = pygame.image.load("./assets/img/dirt.png")
    img_grass = pygame.image.load("./assets/img/grass.png")

    for row_idx, row in enumerate(data):
      for tile_idx, tile in enumerate(row):
        if tile == 1:
          self.__build_tile__(img_dirt, tile_idx, row_idx)
        if tile == 2:
          self.__build_tile__(img_grass, tile_idx, row_idx)

  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])

  def __build_tile__(self, img_name, x_start, y_start):
    img = pygame.transform.scale(img_name, (TILE_SIZE, TILE_SIZE))
    img_rect = img.get_rect()
    img_rect.x = x_start * TILE_SIZE
    img_rect.y = y_start * TILE_SIZE
    tile = (img, img_rect)
    self.tile_list.append(tile)

# Build world
world_data = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 2, 2, 2, 1],
]
world = World(world_data)

# Game loop
run = True

while run :
  screen.blit(img_bg, (0, 0))
  screen.blit(img_sun, (100, 100))

  world.draw()
  draw_grid()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
