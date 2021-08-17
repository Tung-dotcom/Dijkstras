import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208) 

# ^ Defining colours in rgb form - i.e. colour(r, g, b)


class Node: # Creating a class for a node a graph
    def __init__(self, row, col, width, total_rows): 
        self.row = row
        self.col = col
        self.x = col * width # The x co-ordinate will the the column the node is on multiplied by the width of 1 node
        self.y = row * width # ^^ but with y and row 
        self.colour = WHITE
        self.neighbours = []
        self.width = width # Width of 1 node
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED
    
    def is_open(self):
        return self.colour == GREEN
    
    def is_barrier(self):
        return self.colour == BLACK

    def is_start(self):
        return self.colour == ORANGE

    def is_end(self):
        return self.colour == TURQUOISE
    
    # ^^ Methods to check what colour / status a node is 

    def reset(self):
        self.colour = WHITE

    def make_closed(self):
        self.colour = RED
    
    def make_open(self):
        self.colour = GREEN
    
    def make_barrier(self):
        self.colour = BLACK

    def make_start(self):
        self.colour = ORANGE

    def make_end(self):
        self.colour = TURQUOISE
    
    def make_path(self):
        self.colour = PURPLE

    # ^^ Methods to set a colour / status to a node

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width)) 
    # Method to draw the nodes

    def update_neighbours(self, grid):
        self.neighbours = [] 
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN 
            # ^^ Checking if the current node isn't on the bottom row and the node below isn't a barrier
            # self.total_rows - 1 because the list of rows starts from 0 to (n - 1) where n is the number of total rows
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

def make_grid(rows, width):
    grid = []
    gap = width // rows # Gap between each node
    for i in range(rows): # For every row create an empty array inside grid
        grid.append([])
        for j in range(rows): # Create each node by looping throgh the rows again by the number of columns (which is the same as the number of rows) e.g. [[(1,1), (2,1), (3,1)], [(1,2), (2,2), (3,2)], [(1,3), (2,3), (3,3)]] for a 3x3 square
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid

def draw_grid(win, rows, width): # Draw all the grid lines
    gap = width // rows
    for i in range(rows): 
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap)) # Horizontal lines
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width)) # Vertical lines

def draw(win, grid, rows, width):
    win.fill(WHITE) # White background

    for row in grid:
        for node in row:
            node.draw(win) # Colour the node with it's assigned colour
    
    draw_grid(win, rows, width) 
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos # Co-ordinate of mouse click where pos is in (x, y) form

    row = y // gap # The row will be the y co-ordinate divided by size of each node
    col = x // gap # ^^ Same but for x co-ordinate

    return row, col