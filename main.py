import pygame
from grid import Grid
from ui import UI
from best_first_search import best_first_search, heuristic_manhattan, heuristic_euclidean, heuristic_chebyshev
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    grid = Grid()
    ui = UI()
    mode = 'start'
    heuristic = heuristic_manhattan
    heuristic_name = "Manhattan"
    no_path_message = None
    no_path_timer = 0
    visited_count = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                # Check button clicks
                new_mode, new_heuristic, new_heuristic_name = ui.check_button_click(pos)
                if new_mode:
                    mode = new_mode
                if new_heuristic:
                    heuristic = globals()[new_heuristic]  # Convert string to function
                    heuristic_name = new_heuristic_name
                # Grid click
                if pos[1] < WINDOW_SIZE:
                    grid.handle_click(pos, mode)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid.reset_path()
                    path, visited_count = best_first_search(grid, grid.start, grid.end, heuristic)
                    if path:
                        for r, c in path:
                            if grid.grid[r][c] not in [START, END]:
                                grid.grid[r][c] = PATH
                    else:
                        no_path_message = ui.font.render("No path found!", True, RED)
                        no_path_timer = pygame.time.get_ticks()
                elif event.key == pygame.K_r:
                    grid.reset_path()
                    no_path_message = None
                    visited_count = 0

        # Clear no_path_message after 3 seconds
        if no_path_message and (pygame.time.get_ticks() - no_path_timer > 3000):
            no_path_message = None

        ui.draw(grid, mode, heuristic_name, visited_count, no_path_message)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()