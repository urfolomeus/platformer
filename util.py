import pygame

from config import config

# Draw grid (helps us see where things will go on screen)
def draw_grid(screen):
	if config.draw_grid:
		for line in range(0, 20):
			pygame.draw.line(screen, (255, 255, 255), (0, line * config.tile_size), (config.width, line * config.tile_size))
			pygame.draw.line(screen, (255, 255, 255), (line * config.tile_size, 0), (line * config.tile_size, config.height))

def draw_rect(screen, tile):
	if config.draw_rect:
		pygame.draw.rect(screen, (255, 255, 255), tile, 2)