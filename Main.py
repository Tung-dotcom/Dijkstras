import pygame
import Graph
from Dijkstras import dijkstras


WIDTH = 800 # Width of window 
WIN = pygame.display.set_mode((WIDTH, WIDTH)) # Setting window size
pygame.display.set_caption("Dijkstra's Path Finding") # Window title


def main(win, width):
    ROWS = 50 # Change the size of the grid
    grid = Graph.make_grid(ROWS, width)
    #print(grid)

    start = None
    end = None

    run = True

    while run:
        Graph.draw(win, grid, ROWS, width) # Drawing the grid
        for event in pygame.event.get(): # Looping through the events in the queue e.g. keyboard strokes, mouse clicks, etc..
            if event.type == pygame.QUIT: # Quit button on the top right actually closes the window
                run = False

            if pygame.mouse.get_pressed()[0]: # Checking for left mouse button
                pos = pygame.mouse.get_pos() # Position of mouse click in (x, y) form
                row, col = Graph.get_clicked_pos(pos, ROWS, width)  
                node = grid[row][col] 
                if start is None and node != end: # If start hasn't been placed and the node isn't the end node
                    start = node
                    start.make_start()
                
                elif end is None and node != start: # If none hasn't been placed and the node isn't the start node
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # Checking for right mouse button
                pos = pygame.mouse.get_pos()
                row, col = Graph.get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                            
                    dijkstras(lambda: Graph.draw(win, grid, ROWS, width), grid, start, end)
    pygame.quit()

if __name__ == "__main__":
    main(WIN, WIDTH)
