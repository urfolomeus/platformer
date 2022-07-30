import pygame

from config import config

# Draw grid (helps us see where things will go on screen)
def draw_grid(screen):
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * config.tile_size), (config.width, line * config.tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * config.tile_size, 0), (line * config.tile_size, config.height))
