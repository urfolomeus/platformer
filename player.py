import pygame

from config import config

class Player:
  def __init__(self, x, y):
    img = pygame.image.load("./assets/img/guy1.png")
    self.image = pygame.transform.scale(img, config.player_size)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def update(self, screen):
    screen.blit(self.image, self.rect)
