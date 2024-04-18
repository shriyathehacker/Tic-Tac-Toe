from random import choice

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

def sum(num1, num2, num3):
  return num1 + num2 + num3

def move(possibleMoves, board):
  scores = {}

  for i in possibleMoves:
    board2 = board.copy()
    board2[i] = 1 
    scores[i] = miniMax([x for x in possibleMoves if x != i], board2, True, 1)

  indexs = []
  maxValue = -2
  
  for keys, value in scores.items():
    if maxValue < value:
      indexs = [keys]
      maxValue = value
    elif maxValue == value:
      indexs.append(keys)
    
  return choice(indexs)

def miniMax(possibleMoves, board2, player, depth):
  endState = terminal(board2)
  if endState is not None:
    return endState
  else:
    l = []
    for i in possibleMoves:
      if player:
        board2[i] = -1
      else:
        board2[i] = 1
      l.append(miniMax([x for x in possibleMoves if x != i], board2, not player, depth + 1))
      board2[i] = 0

    if player:
      return min(l)
    else:
      return max(l)