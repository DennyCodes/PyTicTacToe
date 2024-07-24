# main.py

# main.py
import random
import time
# start=input("head or tails")
# hr = random.randint(1,2)
# if hr == 1 and start == 'head':
#   #user starts
# elif hr == 2 and start == 'tail'
#   #user starts
# else:
#   #computer starts
#old ai method 
def oldAi(grid):
  aix=random.randint(0,2)
  aiy=random.randint(0,2)
  while grid[aix][aiy] == 'o' or grid[aix][aiy] == 'x':
    aix=random.randint(0,2)
    aiy=random.randint(0,2)
  grid[aix][aiy]='x'
  printGrid(grid)

def newGrid():
  grids=[]
  for i in range(3):
    row=[]
    for j in range(3):
      row.append(' ')
    grids.append(row)
  return grids
def printGrid(grid):

  return
  
#grid=newGrid()



def ai(grid):
  
  if grid[1][1]==' ':
    grid[1][1] = 'o'
    printGrid(grid)
    return
    #winning Horizontaly
  for i in range(3):
    if grid[i][0] == 'o' and grid[i][1] == 'o' and grid[i][2]==' ':
      grid[i][2]='o'
      printGrid(grid)
      return
    elif grid[i][0] == 'o' and grid[i][2] == 'o' and grid[i][1]==' ':
      grid[i][1]='o'
      printGrid(grid)
      return
    elif grid[i][1] == 'o' and grid[i][2] == 'o' and grid[i][0]==' ':
      grid[i][0]='o'
      printGrid(grid)
      return
  #winning vert
  for i in range(3):
    if grid[0][i] == 'o' and grid[1][i] == 'o' and grid[2][i]==' ':
      grid[2][i]='o'
      printGrid(grid)
      return
    elif grid[0][i] == 'o' and grid[2][i] == 'o' and grid[1][i]==' ':
      grid[1][i]='o'
      printGrid(grid)
      return
    elif grid[1][i] == 'o' and grid[2][i] == 'o' and grid[0][i]==' ':
      
      grid[0][i]='o'
      printGrid(grid)
      return
  #winning diag
  if grid[0][0] == 'o' and grid[1][1] == 'o' and grid[2][2]==' ':
    grid[2][2]='o'
    printGrid(grid)
    return
  elif grid[0][0] == 'o' and grid[2][2] == 'o' and grid[1][1]==' ':
    grid[1][1]='o'
    printGrid(grid)
    return
  elif grid[1][1] == 'o' and grid[2][2] == 'o' and grid[0][0]==' ':
    grid[0][0]='o'
    printGrid(grid)
    return
  elif grid[2][0] == 'o' and grid[1][1] == 'o' and grid[0][2]==' ':
    grid[0][2]='o'
    printGrid(grid)
    return
  elif grid[2][0] == 'o' and grid[0][2] == 'o' and grid[1][1]==' ':
    grid[1][1]='o'
    printGrid(grid)
    return
  elif grid[0][2] == 'o' and grid[1][1] == 'o' and grid[2][0]==' ':
    grid[2][0]='o'
    printGrid(grid)
    return
  
 #block Horizontaly
  for i in range(3):
    if grid[i][0] == 'x' and grid[i][1] == 'x' and grid[i][2]==' ':
      grid[i][2]='o'
      printGrid(grid)
      return
    elif grid[i][0] == 'x' and grid[i][2] == 'x' and grid[i][2]==' ':
      grid[i][1]='o'
      printGrid(grid)
      return
    elif grid[i][1] == 'x' and grid[i][2] == 'x' and grid[i][2]==' ':
      grid[i][0]='o'
      printGrid(grid)
      return
  #block vert
  for i in range(3):
    if grid[0][i] == 'x' and grid[1][i] == 'x' and grid[2][i]==' ':
      grid[2][i]='o'
      printGrid(grid)
      return
    elif grid[0][i] == 'x' and grid[2][i] == 'x' and grid[1][i]==' ':
      grid[1][i]='o'
      printGrid(grid)
      return
    elif grid[1][i] == 'x' and grid[2][i] == 'x' and grid[0][i]==' ':
      grid[0][i]='o'
      printGrid(grid)
      return
  #block diag
  if grid[0][0] == 'x' and grid[1][1] == 'x' and grid[2][2]==' ':
    grid[2][2]='o'
    printGrid(grid)
    return
  elif grid[0][0] == 'x' and grid[2][2] == 'x' and grid[1][1]==' ':
    grid[1][1]='o'
    printGrid(grid)
    return
  elif grid[1][1] == 'x' and grid[2][2] == 'x' and grid[0][0]==' ':
    grid[0][0]='o'
    printGrid(grid)
    return
  elif grid[2][0] == 'x' and grid[1][1] == 'x' and grid[0][2]==' ':
    grid[0][2]='o'
    printGrid(grid)
    return
  elif grid[2][0] == 'x' and grid[0][2] == 'x' and grid[1][1]==' ':
    grid[1][1]='o'
    printGrid(grid)
    return
  elif grid[0][2] == 'x' and grid[1][1] == 'x' and grid[2][0]==' ':
    grid[2][0]='o'
    printGrid(grid)
    return
  if grid[0][0] == ' ':
    grid[0][0]='o'
    printGrid(grid)
    return
  elif grid[0][2] == ' ':
    grid[0][2]='o'
    printGrid(grid)
    return
  elif grid[2][0] == ' ':
    grid[2][0]='o'
    printGrid(grid)
    return
  elif grid[2][2] == ' ':
    grid[2][2]='o'
    printGrid(grid)
    return
  
  
  

  aix=random.randint(0,2)
  aiy=random.randint(0,2)
  while grid[aix][aiy] == 'o' or grid[aix][aiy] == 'x':
    aix=random.randint(0,2)
    aiy=random.randint(0,2)
  grid[aix][aiy]='o'
  printGrid(grid)

def gameEnd(grid):
  game=0
  for i in range(3):
    if grid[0][i] == 'x' and grid[1][i] == 'x' and grid[2][i] == 'x':
      game=1
      return game
    elif grid[0][i] == 'o' and grid[1][i] == 'o' and grid[2][i] == 'o':
      game=2
      return game
  for i in range(3):
    if grid[i][0] == 'x' and grid[i][1] == 'x' and grid[i][2] == 'x':
      game=1
      return game
    elif grid[i][0] == 'o' and grid[i][1] == 'o' and grid[i][2] == 'o':
      game=2
      return game
  if grid[0][0] == 'o' and grid[1][1] == 'o' and grid[2][2] == 'o':
    game=2
    return game
  elif grid[0][0] == 'x' and grid[1][1] == 'x' and grid[2][2] == 'x':
    game=1
    return game
  if grid[0][2] == 'o' and grid[1][1] == 'o' and grid[2][0] == 'o':
    game=2
    return game
  elif grid[0][2] == 'x' and grid[1][1] == 'x' and grid[2][0] == 'x':
    game=1
    return game
  
  for i in grid:
    for j in i:
      if j == ' ':
        return game
  game=3
  return game
      
      
  
def winner(grid, game):

  starter=random.randint(0,1)
  if starter == 0:
    while game ==0:
      oldAi(grid)
      if gameEnd(grid) != 0:
        return 1
        break
      ai(grid)
      game=gameEnd(grid)
    if game == 1:
      return 1
    elif game ==2:
      return 2
    else:
      return 3
  elif starter == 1:
    while game ==0:
      ai(grid)
      if gameEnd(grid) != 0:
        return 2
        break
      oldAi(grid)
      game=gameEnd(grid)
    if game == 1:
      return 1
    elif game ==2:
      return 2
    else:
      return 3

def counters():
  counterAI=0
  counterOld=0 
  counterTie=0 

  for i in range(1000):
    game=winner(newGrid(), gameEnd(newGrid()))
    winner(newGrid(), gameEnd(newGrid()))

    print(i)
    if game == 1:
      counterOld+=1 
    elif game ==2:
      counterAI+=1 
    else:
      counterTie+=1
  print(str(counterAI) +" :New Ai")
  print(str(counterOld) +" :Old Ai")
  print(str(counterTie) +" :Tie")
  
counters()

  
      
      

  
#
#he
#
#
#
#

















#
#300!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!