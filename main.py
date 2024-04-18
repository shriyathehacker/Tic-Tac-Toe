import pygame
from game import code

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tic-Tac-Toe")
done = True

class button(pygame.sprite.Sprite):
  def __init__(self, message, x, y, type):
    super().__init__()
    self.image = font.render(message, True, (160, 32, 240))
    self.rect = self.image.get_rect(center = (x, y))
    self.type = type
    
  def activate(self):
    code(self.type)
    
titleSurface = pygame.image.load("tictactoelogo.png").convert_alpha()
titleSurface.set_colorkey((255, 255, 255))
titleRect = titleSurface.get_rect(midtop = (400, 0))

font = pygame.font.Font("Risque-Regular.otf", 100)

button1 = button("Player Start", 400, 250, True)
button2 = button("AI Start", 400, 400, False)
buttonsGroup = pygame.sprite.Group()
buttonsGroup.add(button1, button2)

file = open("currentScores.txt", "r")
intList = [str(x) for x in file.readline().split()]
file.close()
intList.reverse()

scoreSurface = font.render("-".join(intList), True, (160, 32, 240))
scoreRect = scoreSurface.get_rect(center = ((400, 550)))

while done:
  screen.fill((255, 200, 200))
  screen.blit(titleSurface, titleRect)
  screen.blit(scoreSurface, scoreRect)
  buttonsGroup.draw(screen)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      for buttons in buttonsGroup:
        if buttons.rect.collidepoint(event.pos):
          buttons.activate()
          file = open("currentScores.txt", "r")
          intList = [str(x) for x in file.readline().split()]
          file.close()
          intList.reverse()

          scoreSurface = font.render("-".join(intList), True, (160, 32, 240))

  pygame.display.flip()

pygame.quit()