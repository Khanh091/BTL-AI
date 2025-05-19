from heapq import heappush, heappop
from constants import *

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def best_first_search(grid, start, end):
    if not start or not end:
        return []

    open_list = []
    heappush(open_list, (heuristic(start, end), start))
    came_from = {}
    visited = set()

    while open_list:
        _, current = heappop(open_list)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, down, left, right
            r, c = current[0] + dr, current[1] + dc
            neighbor = (r, c)
            if (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and
                grid.grid[r][c] != WALL and neighbor not in visited):
                came_from[neighbor] = current
                heappush(open_list, (heuristic(neighbor, end), neighbor))

    return []  # No path found