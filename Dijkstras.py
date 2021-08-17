import pygame
from queue import PriorityQueue

def reconstruct_path(came_from, current, draw):
    while current in came_from: 
        current = came_from[current] 
        current.make_path()
        draw()

def dijkstras(draw, grid, start, end): 
    open_set  = PriorityQueue() # A queue where all the elements are sorted from smallest to largest
    open_set.put((0, start)) # Distance of start node is 0
    came_from = {}
    distance = {node: float('inf') for row in grid for node in row} # Distance infinity for all nodes apart from start as distance is unknown
    distance[start] = 0 # Distance of start node is 0

    open_set_hash = {start} # Need as you cannot check if there are elements in a priority queue

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[1] # Getting the node itself
        open_set_hash.remove(current) 

        if current == end:
            reconstruct_path(came_from, end, draw)
            start.make_start()
            end.make_end()
            return True
        
        
        for neighbour in current.neighbours:
            temp_distance = distance[current] + 1 # Each edge has a distance of 1
            if temp_distance < distance[neighbour]: # Checking for better path
                came_from[neighbour] = current # Setting the current node as the node each of it's neighbours came from
                distance[neighbour] = temp_distance 
                if neighbour not in open_set_hash:
                    open_set.put((distance[neighbour], neighbour)) # Add to the open set
                    open_set_hash.add(neighbour)
                    neighbour.make_open() # Change to green
                
        draw()
        if current != start: # Close the node off as it's been considered already (Equivilant to giving the node a final label)
            current.make_closed() # Change to red

    return False