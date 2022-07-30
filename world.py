import pygame

import util
from config import config
from enemy import Enemy

class World:
  def __init__(self, data, blob_group):
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
        if tile == 3:
          blob = Enemy(tile_idx * config.tile_size, row_idx * config.tile_size)
          blob_group.add(blob)

  def draw(self, screen):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])
      util.draw_rect(screen, tile[1])

  def __build_tile__(self, img_name, x_start, y_start):
    img = pygame.transform.scale(img_name, (config.tile_size, config.tile_size))
    img_rect = img.get_rect()
    img_rect.x = x_start * config.tile_size
    img_rect.y = y_start * config.tile_size
    tile = (img, img_rect)
    self.tile_list.append(tile)
