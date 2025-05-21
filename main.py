import pygame
from grid import Grid
from best_first_search import best_first_search, heuristic_manhattan, heuristic_euclidean, heuristic_chebyshev
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Best First Search Pathfinding")
    clock = pygame.time.Clock()
    grid = Grid()
    mode = 'start'
    heuristic = heuristic_manhattan
    heuristic_name = "Manhattan"
    font = pygame.font.SysFont("arial", 20)
    no_path_message = None
    no_path_timer = 0

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
                elif event.key == pygame.K_d:  # Use D for End to avoid conflict with E
                    mode = 'end'
                elif event.key == pygame.K_w:
                    mode = 'wall'
                elif event.key == pygame.K_m:
                    heuristic = heuristic_manhattan
                    heuristic_name = "Manhattan"
                elif event.key == pygame.K_e:
                    heuristic = heuristic_euclidean
                    heuristic_name = "Euclidean"
                elif event.key == pygame.K_c:
                    heuristic = heuristic_chebyshev
                    heuristic_name = "Chebyshev"
                elif event.key == pygame.K_SPACE:
                    grid.reset_path()
                    path = best_first_search(grid, grid.start, grid.end, heuristic)
                    if path:
                        for r, c in path:
                            if grid.grid[r][c] not in [START, END]:
                                grid.grid[r][c] = PATH
                    else:
                        no_path_message = font.render("No path found!", True, RED)
                        no_path_timer = pygame.time.get_ticks()  # Start timer
                elif event.key == pygame.K_r:
                    grid.reset_path()
                    no_path_message = None  # Clear message on reset

        # Clear no_path_message after 3 seconds
        if no_path_message and (pygame.time.get_ticks() - no_path_timer > 3000):
            no_path_message = None

        screen.fill(WHITE)
        grid.draw(screen)
        # Display current mode and heuristic
        mode_text = font.render(f"Mode: {mode.capitalize()}", True, BLACK)
        heuristic_text = font.render(f"Heuristic: {heuristic_name}", True, BLACK)
        screen.blit(mode_text, (10, WINDOW_SIZE - 50))
        screen.blit(heuristic_text, (10, WINDOW_SIZE - 30))
        # Display no path message if exists
        if no_path_message:
            screen.blit(no_path_message, (WINDOW_SIZE // 2 - 50, WINDOW_SIZE // 2))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()