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
    self.__move()
    screen.blit(self.image, self.rect)

  def __move(self):
    dx = 0
    dy = 0

    # get keypresses
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
      dx -= config.player_step_size
    elif key[pygame.K_RIGHT]:
      dx += config.player_step_size

    # check for collisions

    # update player coordinates
    self.rect.x += dx
    self.rect.y += dy