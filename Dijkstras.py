import pygame
from queue import PriorityQueue

def reconstruct_path(came_from, current, draw, start):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        start.make_start()
        draw()

def dijkstras(draw, grid, start, end): 
    open_set  = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    distance = {node: float('inf') for row in grid for node in row} # Distance infinity for all nodes apart from start as distance is unknown
    distance[start] = 0

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[1]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw, start)
            end.make_end()
            return True
        
        
        for neighbour in current.neighbours:
            temp_distance = distance[current] + 1

            if temp_distance < distance[neighbour]:
                came_from[neighbour] = current
                distance[neighbour] = temp_distance
                if neighbour not in open_set_hash:
                    open_set.put((distance[neighbour], neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
                
        draw()

        if current != start:
            current.make_closed()

    return False