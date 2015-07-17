import random
from grouper import Grouper
import sys

X = 60
Y = 60

class Cell():
    
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.right_wall = self.down_wall = None

class Wall():
    
    def __init__(self):
        self.neighbours = None
        self.active = True

def popchoice(seq):
   
    return seq.pop(random.randrange(len(seq)))

cells = {}
walls = []

for y in range(Y):
    for x in range(X):
        cells[(x, y)] = Cell(x, y)

for y in range(Y):
    for x in range(X):
        current_cell = cells[(x,y)]
        down_wall = Wall()
        current_cell.down_wall = down_wall
        right_wall = Wall()
        current_cell.right_wall = right_wall
        if y != Y-1:
            down_wall.neighbours = (current_cell, cells[(x,y+1)])
            walls.append(down_wall)

        if x != X-1:
            right_wall.neighbours = (current_cell, cells[(x+1,y)])
            walls.append(right_wall)


cell_list = [cells[key] for key in cells]

maze = Grouper(cell_list)

for _ in range(len(walls)):
    
    wall = popchoice(walls)
    cell_1, cell_2 = wall.neighbours
    
    if not maze.joined(cell_1, cell_2):
        wall.active = False
        maze.join(cell_1, cell_2)



maze_map = []

x_max = (X*2)+1
y_max = (Y*2)+1

maze_map.append([True for _ in range(x_max)])
for y in range(1, y_max):
    maze_map.append([True]+[False for _ in range(1, x_max)])


for coords, cell in cells.items():
    x, y = coords

    maze_map[(y*2)+2][(x*2)+2] = True
    if cell.right_wall.active:
        maze_map[(y*2)+1][(x*2)+2] = True
    if cell.down_wall.active:
        maze_map[(y*2)+2][(x*2)+1] = True

def output(string):
    sys.stdout.write(string)


matriz = []

for i, x in enumerate(maze_map):
    matriz.append([])
    #del x[-2]
    for j in x:
        if j:
            matriz[i].append('X')
        else:
            matriz[i].append('0')

#del matriz[-2]

 