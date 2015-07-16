import random
from grouper import Grouper
import sys

X = 3
Y = 3

class Cell():
    """Represents a cell in the maze, with an x and y coordinate and its
    right hand wall and downwards wall.

    """
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.right_wall = self.down_wall = None

class Wall():
    """Represents a wall in the maze with its two neighbouring cells.
    """
    def __init__(self):
        self.neighbours = None
        self.active = True

def popchoice(seq):
    """Takes an iterable and pops a random item from it.
    """
    return seq.pop(random.randrange(len(seq)))

# A mapping of coord tuple to Cell object    
cells = {}
# A list of all the non-edge walls
walls = []

# Generate cells
for y in range(Y):
    for x in range(X):
        cells[(x, y)] = Cell(x, y)

# Generate walls and add to the neighbouring cells
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


# Get a list of all the cell objects to give to the Grouper            
cell_list = [cells[key] for key in cells]

maze = Grouper(cell_list)

for _ in range(len(walls)):
    # Pop a random wall from the list and get its neighbours
    wall = popchoice(walls)
    cell_1, cell_2 = wall.neighbours
    # If the cells on either side of the wall aren't already connected,
    # destroy the wall
    if not maze.joined(cell_1, cell_2):
        wall.active = False
        maze.join(cell_1, cell_2)

# Draw the maze

maze_map = []

x_max = (X*2)+1
y_max = (Y*2)+1

# Make an empty maze map with True for wall and False for space
# Make top wall
maze_map.append([True for _ in range(x_max)])
for y in range(1, y_max):
    # Make rows with left side wall
    maze_map.append([True]+[False for _ in range(1, x_max)])

# Add the down and right walls from each cell to the map
for coords, cell in cells.items():
    x, y = coords
    # Add the intersection wall for each cell (down 1 right 1)
    maze_map[(y*2)+2][(x*2)+2] = True
    if cell.right_wall.active:
        maze_map[(y*2)+1][(x*2)+2] = True
    if cell.down_wall.active:
        maze_map[(y*2)+2][(x*2)+1] = True

def output(string):
    sys.stdout.write(string)

# Print the map
#for row in maze_map:
#    for tick in row:
#        if tick: output('X '),
#        else: output('0 '),
#    output('\n')


matriz = []

for i, x in enumerate(maze_map):
    matriz.append([])
    del x[-2]
    for j in x:
        if j:
            matriz[i].append('X')
        else:
            matriz[i].append('0')

del matriz[-2]

 