import pygame
from pygame.locals import *
from button import Button

import util
from config import config
from player import Player
from world import World

PLAYER_START_X = 100

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.title)

# Load assets
img_bg = pygame.image.load("./assets/img/sky.png")
img_exit = pygame.image.load("./assets/img/exit_btn.png")
img_restart = pygame.image.load("./assets/img/restart_btn.png")
img_start = pygame.image.load("./assets/img/start_btn.png")
img_sun = pygame.image.load("./assets/img/sun.png")

# Create buttons
exit_button = Button(img_exit, config.width // 2 + 150, config.height // 2)
restart_button = Button(img_restart, config.width // 2 - 50, config.height // 2 - 100)
start_button = Button(img_start, config.width // 2 - 350, config.height // 2)

# Create objects
player = Player()
blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()

# Build world
world_data = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
  [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
  [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
  [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
  [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
  [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
  [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
  [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
  [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
  [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

world = World(world_data, blob_group, lava_group)

game_context = {
  "world": world,
  "blob_group": blob_group,
  "lava_group": lava_group,
  "game_over": 0,
  "show_main_menu": True,
}

# Game loop
run = True

while run :
  clock.tick(config.fps)

  screen.blit(img_bg, (0, 0))
  screen.blit(img_sun, (100, 100))

  if game_context["show_main_menu"]:
    exit_button.draw(screen)
    if exit_button.clicked():
      run = False
    
    start_button.draw(screen)
    if start_button.clicked():
      game_context["show_main_menu"] = False
  else:
    world.draw(screen)

    util.draw_grid(screen)

    game_context = player.update(screen, game_context)

    if game_context["game_over"] == 0:
      blob_group.update()
    blob_group.draw(screen)

    lava_group.draw(screen)

    if game_context["game_over"] == -1:
      restart_button.draw(screen)
      if restart_button.clicked():
        player.reset()
        game_context["game_over"] = 0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
