import pygame

import util
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

    self.dead_image = pygame.image.load("./assets/img/ghost.png")
    
    self.__update_image()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y


  def update(self, screen, game_context):
    if game_context["game_over"] == -1:
      self.image = self.dead_image
      if self.rect.y > 200:
        self.rect.y -= 5
    else:
      game_context = self.__move(game_context)
    
    screen.blit(self.image, self.rect)
    util.draw_rect(screen, self.rect)
    
    return game_context

  def __move(self, game_context):
    dx = 0
    dy = 0

    dx = self.__handle_keypress(dx)
    self.__animate()
    self.__simulate_gravity()
    dy += self.vel_y
    (dx, dy, game_context) = self.__check_for_collisions(dx, dy, game_context)

    # update player coordinates
    self.rect.x += dx
    self.rect.y += dy

    return game_context

  def __animate(self):
    walk_cooldown = 5

    if self.counter > walk_cooldown:
      self.counter = 0
      self.current_index += 1
      if self.current_index >= len(self.images[self.direction]):
        self.current_index = 0
      self.__update_image()

  def __check_for_collisions(self, dx, dy, game_context):
    for tile in game_context["world"].tile_list:
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

    if pygame.sprite.spritecollide(self, game_context["blob_group"], False):
      game_context["game_over"] = -1

    if pygame.sprite.spritecollide(self, game_context["lava_group"], False):
      game_context["game_over"] = -1

    return (dx, dy, game_context)

  def __handle_keypress(self, dx):
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
      self.__update_image()

    return dx

  def __simulate_gravity(self):
    self.vel_y += config.gravity

    if self.vel_y == 10:
      self.vel_y = 10

  def __update_image(self):
    self.image = self.images[self.direction][self.current_index]
