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
def newGrid():
  grids=[]
  for i in range(3):
    row=[]
    for j in range(3):
      row.append(' ')
    grids.append(row)
  return grids
def printGrid(grid):
  print(grid[0][0]+"  | "+grid[0][1]+"  | "+grid[0][2])
  print("------------")
  print(grid[1][0]+"  | "+grid[1][1]+"  | "+grid[1][2])
  print("------------")
  print(grid[2][0]+"  | "+grid[2][1]+"  | "+grid[2][2])
  
grid=newGrid()
# grid[0][0]='x'
# print(printGrid(grid))
def player(grid):
  #usrInput = input("Pick a place to input. (e.g. grid[x][y], would be bottom row)")
  
  usrInputx= int(input("Put in a x value: "))
  usrInputy= int(input("Put in a y value: "))
  if usrInputx >= 3 or usrInputy >=3 or usrInputx <0 or usrInputy <0:
    print("try again. Invalid location")
    return False
  e=grid[usrInputx][usrInputy]
  if e == ' ':
    grid[usrInputx][usrInputy] = 'x'
    printGrid(grid)
  elif e == 'o':
    print("you can't go there. (taken)")
    player(grid)
  elif e == 'x':
    print("You have already been there.")
    player(grid)
  else:
    print("You can't go there. (out of range)")
    player(grid)

def ai(grid):
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
      
      
  
def turns(grid, game):
  start=input("heads or tails: ")
  hr = random.randint(1,2)
  if hr == 1 and start == 'heads':
    #user starts
    while game == 0:
      player(grid)
      print("-------------------------------------------------------------")
      if gameEnd(grid) != 0:
        print("player won")
        break
      time.sleep(1.2)
      ai(grid)
      print("-------------------------------------------------------------")
      game=gameEnd(grid)
    if game == 1:
      print("The Player Won")
    if game ==2:
      print("AI won")
    
  elif hr == 2 and start == 'tails':
    #user starts
    while game == 0:
      
      player(grid)
      print("-------------------------------------------------------------")
      if gameEnd(grid) != 0:
        print("player won")
        break
      time.sleep(1.2)
      ai(grid)
      print("-------------------------------------------------------------")
      game=gameEnd(grid)
    if game == 1:
      print("The Player Won")
    if game ==2:
      print("AI won")
  else:
    #computer starts
    while game ==0:
      ai(grid)
      print("-------------------------------------------------------------")
      if gameEnd(grid) != 0:
        print("ai won")
        break
      time.sleep(1.2)
      player(grid)
      if gameEnd(grid) != 0:
        break
      print("-------------------------------------------------------------")
      game=gameEnd(grid)
    if game == 1:
      print("The Player Won")
    if game ==2:
      print("AI won")
  if game == 3:
    print("game ended. (tie) (no more spaces left)")
turns(grid, gameEnd(grid))
  
#
