import pygame

from config import config


class Lava(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    
    img = pygame.image.load("./assets/img/lava.png")
    self.image = pygame.transform.scale(img, (config.tile_size, config.tile_size // 2))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y + (config.tile_size // 2)
