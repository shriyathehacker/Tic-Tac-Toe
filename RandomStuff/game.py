import pygame
import sys
from RandomStuff import ai
from time import sleep
from random import randint

def code(flag):
  class Tile(pygame.sprite.Sprite):
    def __init__(self, state, position, count):
      super().__init__()
      self.id = count
      self.state = state
      self.image = pygame.Surface((200, 200), pygame.SRCALPHA)
      self.rect = self.image.get_rect(center = convert(position[0], position[1]))
      self.filled = False
      self.pos = (3 * position[1]) + position[0] 
  
    def click(self, flag):
      if not(self.filled):
        if flag:
          self.cross((255, 0, 0))
          self.filled = True
          array[self.pos] = -1
          return False
        else:
          self.circle((0, 0, 255))
          self.filled = True
          array[self.pos] = 1
          return True
      else:
        if flag:
          return True
        else:
          return False
  
    def cross(self, color):
      pygame.draw.line(self.image, color, (10, 10), (190, 190), width=5)
      pygame.draw.line(self.image, color, (10, 190), (190, 10), width=5)
  
    def circle(self, color):
      pygame.draw.circle(self.image, color, (100, 100), 90, width=5)
  
  def board(screen, color):
    pygame.draw.line(screen, color, (0, 200), (600, 200), width=5)
    pygame.draw.line(screen, color, (0, 400), (600, 400), width=5)
    pygame.draw.line(screen, color, (200, 0), (200, 600), width=5)
    pygame.draw.line(screen, color, (400, 0), (400, 600), width=5)
  
  def convert(x, y):
    return ((200 * x) + 100, (200 * y) + 100)
  
  def sum(a, b, c):
    return a + b + c
  
  def actions(array):
    possibleMoves = []
    for index in range(len(array)):
      if array[index] == 0:
        possibleMoves.append(index)
  
    return possibleMoves
  
  def terminal(array):
    if abs(sum(array[0], array[1], array[2])) == 3:
      return sum(array[0], array[1], array[2]) // 3
    
    elif abs(sum(array[3], array[4], array[5])) == 3:
      return sum(array[3], array[4], array[5]) // 3
    
    elif abs(sum(array[6], array[7], array[8])) == 3:
      return sum(array[6], array[7], array[8]) // 3
    
    elif abs(sum(array[0], array[3], array[6])) == 3:
      return sum(array[0], array[3], array[6]) // 3
    
    elif abs(sum(array[1], array[4], array[7])) == 3:
      return sum(array[1], array[4], array[7]) // 3
    
    elif abs(sum(array[2], array[5], array[8])) == 3:
      return sum(array[2], array[5], array[8]) // 3
    
    elif abs(sum(array[0], array[4], array[8])) == 3:
      return sum(array[0], array[4], array[8]) // 3
    
    elif abs(sum(array[2], array[4], array[6])) == 3:
      return sum(array[2], array[4], array[6]) // 3
    
    elif 0 not in array:
      return 0
    
    return None

  def fileSort(value):
    fin = open("RandomStuff/currentScores.txt", "r")
    intList = [int(x) for x in fin.readline().split()]

    if value == 1:
      intList[0] += 1
    elif value == 0:
      intList[1] += 1
    else:
      intList[2] += 1

    fout = open("RandomStuff/currentScores.txt", "w")
    fout.write(" ".join(map(str, intList)))
    fout.close()
        
  
  screen = pygame.display.set_mode((800, 600))
  done = True
  array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  
  tileGroup = pygame.sprite.Group()

  font = pygame.font.Font("RandomStuff/Risque-Regular.otf", 50)

  text1Surface = font.render("AI", True, (160, 32, 240))
  text1Rect = text1Surface.get_rect(midleft = (610, 200))

  text2Surface = font.render("Player", True, (160, 32, 240))
  text2Rect = text2Surface.get_rect(midleft = (610, 400))
  
  count = 0
  for i in range(3):
    for j in range(3):
      tileGroup.add(Tile(state = None, position = (j, i), count=count))
      count += 1
  
  while done:
    screen.fill((255, 200, 200))
    tileGroup.draw(screen)
    board(screen, (0, 255, 255))
    screen.blit(text1Surface, text1Rect)
    screen.blit(text2Surface, text2Rect)

    if not(flag):
      pygame.draw.polygon(screen, (160, 32, 240), ((750, 200), (790, 175), (790, 225)))
    else:
      pygame.draw.polygon(screen, (160, 32, 240), ((750, 400), (790, 375), (790, 425)))
      
    pygame.display.flip()
      
    currentState = terminal(array)
    if currentState != None:
      fileSort(currentState)
      done = False
  
    if not(flag):
      possibleMoves = actions(array)
      if possibleMoves != []:
        position = ai.move(possibleMoves, array)
        for tile in tileGroup:
          if tile.id == position:
            flag = tile.click(flag)
  
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = False
  
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for i in tileGroup:
          if i.rect.collidepoint(event.pos):
            if flag:
              flag = i.click(flag)
  
      if event.type == pygame.KEYDOWN:
        print(*array)

  sleep(1)
  pygame.image.save(screen, "final.png")