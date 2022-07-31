import pygame


class Button():
  def __init__(self, image, x, y):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

    self.clicked = False

  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def restart_clicked(self):
    action = False
    pos = pygame.mouse.get_pos()

    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
        action = True
        self.clicked = True

      if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False
    
    return action
