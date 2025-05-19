import pygame
from grid import Grid
from best_first_search import best_first_search
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Best First Search Pathfinding")
    clock = pygame.time.Clock()
    grid = Grid()
    mode = 'start'
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                grid.handle_click(event.pos, mode)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    mode = 'start'
                elif event.key == pygame.K_e:
                    mode = 'end'
                elif event.key == pygame.K_w:
                    mode = 'wall'
                elif event.key == pygame.K_SPACE:
                    grid.reset_path()
                    path = best_first_search(grid, grid.start, grid.end)
                    for r, c in path:
                        if grid.grid[r][c] not in [START, END]:
                            grid.grid[r][c] = PATH
                elif event.key == pygame.K_r:
                    grid.reset_path()

        screen.fill(WHITE)
        grid.draw(screen)
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()