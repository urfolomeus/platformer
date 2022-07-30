import pygame

from config import config

class Player:
  def __init__(self, x, y):
    img = pygame.image.load("./assets/img/guy1.png")
    self.image = pygame.transform.scale(img, config.player_size)
    
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

    self.vel_y = 0
    self.jumped = False

  def update(self, screen):
    self.__move()
    screen.blit(self.image, self.rect)

  def __move(self):
    dx = 0
    dy = 0

    # get keypresses
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and not self.jumped:
      self.vel_y = config.jump_height
      self.jumped = True
    if not key[pygame.K_SPACE]:
      self.jumped = False
    if key[pygame.K_LEFT]:
      dx -= config.player_step_size
    if key[pygame.K_RIGHT]:
      dx += config.player_step_size

    self.__simulate_gravity()

    dy += self.vel_y

    # check for collisions

    # update player coordinates
    self.rect.x += dx
    self.rect.y += dy

    if self.rect.bottom > config.height:
      self.rect.bottom = config.height
      dy = 0

  def __simulate_gravity(self):
    self.vel_y += config.gravity

    if self.vel_y == 10:
      self.vel_y = 10