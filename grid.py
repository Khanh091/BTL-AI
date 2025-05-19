import pygame
from constants import *

class Grid:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.start = None
        self.end = None

    def draw(self, screen):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if self.grid[row][col] == EMPTY:
                    pygame.draw.rect(screen, WHITE, rect)
                elif self.grid[row][col] == WALL:
                    pygame.draw.rect(screen, BLACK, rect)
                elif self.grid[row][col] == START:
                    pygame.draw.rect(screen, GREEN, rect)
                elif self.grid[row][col] == END:
                    pygame.draw.rect(screen, RED, rect)
                elif self.grid[row][col] == PATH:
                    pygame.draw.rect(screen, YELLOW, rect)
                pygame.draw.rect(screen, GRAY, rect, 1)  # Draw grid lines

    def handle_click(self, pos, mode):
        col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            if mode == 'start' and self.grid[row][col] != END:
                if self.start:
                    self.grid[self.start[0]][self.start[1]] = EMPTY
                self.grid[row][col] = START
                self.start = (row, col)
            elif mode == 'end' and self.grid[row][col] != START:
                if self.end:
                    self.grid[self.end[0]][self.end[1]] = EMPTY
                self.grid[row][col] = END
                self.end = (row, col)
            elif mode == 'wall':
                if self.grid[row][col] not in [START, END]:
                    self.grid[row][col] = WALL if self.grid[row][col] == EMPTY else EMPTY

    def reset_path(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == PATH:
                    self.grid[row][col] = EMPTY