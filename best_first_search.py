from heapq import heappush, heappop
from constants import *

def heuristic_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def heuristic_euclidean(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5  # Euclidean distance

def heuristic_chebyshev(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))  # Chebyshev distance

def best_first_search(grid, start, end, heuristic_func=heuristic_manhattan):
    if not start or not end:
        return [], 0

    open_list = []
    heappush(open_list, (heuristic_func(start, end), start))
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
            return path[::-1], len(visited)

        if current in visited:
            continue
        visited.add(current)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, down, left, right
            r, c = current[0] + dr, current[1] + dc
            neighbor = (r, c)
            if (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and
                grid.grid[r][c] != WALL and neighbor not in visited):
                came_from[neighbor] = current
                heappush(open_list, (heuristic_func(neighbor, end), neighbor))

    return [], len(visited)  # No path found