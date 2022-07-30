import pygame

from config import config

class Player:
  def __init__(self, x, y):
    self.images = {
      "left": [],
      "right": [],
    }
    self.index = 0
    self.counter = 0
    self.direction = "right"

    for num in range(1, 5):
      img = pygame.image.load(f"./assets/img/guy{num}.png")
      img_right = pygame.transform.scale(img, config.player_size)
      img_left = pygame.transform.flip(img_right, True, False)
      self.images["right"].append(img_right)
      self.images["left"].append(img_left)
    
    self.image = self.images[self.direction][self.index]
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
    walk_cooldown = 5

    # get keypresses
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and not self.jumped:
      self.vel_y = config.jump_height
      self.jumped = True
    if not key[pygame.K_SPACE]:
      self.jumped = False
    if key[pygame.K_LEFT]:
      dx -= config.player_step_size
      self.counter += 1
      self.direction = "left"
    if key[pygame.K_RIGHT]:
      dx += config.player_step_size
      self.counter += 1
      self.direction = "right"
    if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
      self.counter = 0
      self.index = 0
      self.image = self.images[self.direction][self.index]

    # handle animation
    if self.counter > walk_cooldown:
      self.counter = 0
      self.index += 1
      if self.index >= len(self.images[self.direction]):
        self.index = 0
      self.image = self.images[self.direction][self.index]

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
