import pygame

from config import config

class Player:
  def __init__(self, x, y):
    self.current_index = 0
    self.counter = 0
    self.direction = "right"
    self.jumped = False
    self.vel_y = 0

    self.images = { "left": [], "right": [] }

    for num in range(1, 5):
      img = pygame.image.load(f"./assets/img/guy{num}.png")
      
      img_right = pygame.transform.scale(img, config.player_size)
      self.images["right"].append(img_right)
      
      img_left = pygame.transform.flip(img_right, True, False)
      self.images["left"].append(img_left)
    
    self.image = self.images[self.direction][self.current_index]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y


  def update(self, screen, world):
    self.__move(world)
    screen.blit(self.image, self.rect)
    pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

  def __move(self, world):
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
      self.counter += 1
      self.direction = "left"
    if key[pygame.K_RIGHT]:
      dx += config.player_step_size
      self.counter += 1
      self.direction = "right"
    if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
      self.counter = 0
      self.current_index = 0
      self.image = self.images[self.direction][self.current_index]

    self.__animate()

    self.__simulate_gravity()

    dy += self.vel_y

    # check for collisions
    for tile in world.tile_list:
      # check for collisions in x direction
      if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.image.get_width(), self.image.get_height()):
        dx = 0

      # check for collisions in y direction
      if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()):
        # check if jumping or falling
        if self.vel_y < 0:
          dy = tile[1].bottom - self.rect.top
          self.vel_y = 0
        else:
          dy = tile[1].top - self.rect.bottom
          self.vel_y = 0

    # update player coordinates
    self.rect.x += dx
    self.rect.y += dy

    if self.rect.bottom > config.height:
      self.rect.bottom = config.height
      dy = 0

  def __animate(self):
    walk_cooldown = 5

    if self.counter > walk_cooldown:
      self.counter = 0
      self.current_index += 1
      if self.current_index >= len(self.images[self.direction]):
        self.current_index = 0
      self.image = self.images[self.direction][self.current_index]

  def __simulate_gravity(self):
    self.vel_y += config.gravity

    if self.vel_y == 10:
      self.vel_y = 10
