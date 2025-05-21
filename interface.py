import pygame
from grid import Grid
from constants import *

class Interface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
        pygame.display.set_caption("Best First Search Pathfinding")
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.mode = 'start'
        self.heuristic_name = "Manhattan"
        self.font = pygame.font.SysFont("arial", 20)
        self.no_path_message = None
        self.no_path_timer = 0
        self.visited_count = 0
        self.button_width, self.button_height = 100, 40
        self.buttons = [
            {"text": "Start", "rect": pygame.Rect(10, WINDOW_SIZE + 10, self.button_width, self.button_height), "mode": "start"},
            {"text": "End", "rect": pygame.Rect(120, WINDOW_SIZE + 10, self.button_width, self.button_height), "mode": "end"},
            {"text": "Wall", "rect": pygame.Rect(230, WINDOW_SIZE + 10, self.button_width, self.button_height), "mode": "wall"},
            {"text": "Run", "rect": pygame.Rect(340, WINDOW_SIZE + 10, self.button_width, self.button_height), "action": "run_algorithm"},
            {"text": "Manhattan", "rect": pygame.Rect(10, WINDOW_SIZE + 60, self.button_width, self.button_height), "heuristic_name": "Manhattan"},
            {"text": "Euclidean", "rect": pygame.Rect(120, WINDOW_SIZE + 60, self.button_width, self.button_height), "heuristic_name": "Euclidean"},
            {"text": "Chebyshev", "rect": pygame.Rect(230, WINDOW_SIZE + 60, self.button_width, self.button_height), "heuristic_name": "Chebyshev"},
        ]

    def draw_button(self, text, rect, active):
        color = BLUE if active else GRAY
        pygame.draw.rect(self.screen, color, rect)
        text_surf = self.font.render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for button in self.buttons:
                    if button["rect"].collidepoint(pos):
                        if "mode" in button:
                            self.mode = button["mode"]
                        if "heuristic_name" in button:
                            self.heuristic_name = button["heuristic_name"]
                        if "action" in button:
                            print(f"Button {button['text']} clicked, triggering {button['action']}")  # Debug
                            return True, button["action"]
                if pos[1] < WINDOW_SIZE:
                    self.grid.handle_click(pos, self.mode)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space pressed, triggering run_algorithm")  # Debug
                    return True, "run_algorithm"
                elif event.key == pygame.K_r:
                    print("Reset pressed")  # Debug
                    self.grid.reset_path()
                    self.no_path_message = None
                    self.visited_count = 0
        return True, None

    def update_display(self):
        if self.no_path_message and (pygame.time.get_ticks() - self.no_path_timer > 3000):
            self.no_path_message = None

        self.screen.fill(WHITE)
        self.grid.draw(self.screen)
        for button in self.buttons:
            active = self.mode == button.get("mode") or self.heuristic_name == button.get("heuristic_name")
            self.draw_button(button["text"], button["rect"], active)
        visited_text = self.font.render(f"Visited: {self.visited_count}", True, BLACK)
        self.screen.blit(visited_text, (WINDOW_SIZE - 100, WINDOW_SIZE + 10))
        if self.no_path_message:
            self.screen.blit(self.no_path_message, (WINDOW_SIZE // 2 - 50, WINDOW_SIZE // 2))
        pygame.display.flip()
        self.clock.tick(60)

    def show_no_path(self):
        self.no_path_message = self.font.render("No path found!", True, RED)
        self.no_path_timer = pygame.time.get_ticks()

    def apply_path(self, path):
        for r, c in path:
            if self.grid.grid[r][c] not in [START, END]:
                self.grid.grid[r][c] = PATH

    def run(self):
        running = True
        while running:
            running, action = self.handle_events()
            if action == "run_algorithm":
                yield "run_algorithm"
            self.update_display()
        pygame.quit()

    def get_grid(self):
        return self.grid

    def get_heuristic_name(self):
        return self.heuristic_name

    def set_visited_count(self, count):
        self.visited_count = count