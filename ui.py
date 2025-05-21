import pygame
from constants import *

class UI:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
        pygame.display.set_caption("Best First Search Pathfinding")
        self.font = pygame.font.SysFont("arial", 20)
        self.button_width, self.button_height = 100, 40
        self.buttons = [
            {"text": "Start", "rect": pygame.Rect(10, WINDOW_SIZE + 10, self.button_width, self.button_height), "mode": "start"},
            {"text": "End", "rect": pygame.Rect(120, WINDOW_SIZE + 10, self.button_width, self.button_height), "mode": "end"},
            {"text": "Wall", "rect": pygame.Rect(230, WINDOW_SIZE + 10, self.button_width, self.button_height), "mode": "wall"},
            {"text": "Manhattan", "rect": pygame.Rect(10, WINDOW_SIZE + 60, self.button_width, self.button_height), "heuristic": "heuristic_manhattan", "heuristic_name": "Manhattan"},
            {"text": "Euclidean", "rect": pygame.Rect(120, WINDOW_SIZE + 60, self.button_width, self.button_height), "heuristic": "heuristic_euclidean", "heuristic_name": "Euclidean"},
            {"text": "Chebyshev", "rect": pygame.Rect(230, WINDOW_SIZE + 60, self.button_width, self.button_height), "heuristic": "heuristic_chebyshev", "heuristic_name": "Chebyshev"},
        ]

    def draw_button(self, text, rect, active):
        color = BLUE if active else GRAY
        pygame.draw.rect(self.screen, color, rect)
        text_surf = self.font.render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def draw(self, grid, mode, heuristic_name, visited_count, no_path_message):
        self.screen.fill(WHITE)
        grid.draw(self.screen)
        # Draw buttons
        for button in self.buttons:
            active = mode == button.get("mode") or heuristic_name == button.get("heuristic_name")
            self.draw_button(button["text"], button["rect"], active)
        # Display visited count
        visited_text = self.font.render(f"Visited: {visited_count}", True, BLACK)
        self.screen.blit(visited_text, (WINDOW_SIZE - 100, WINDOW_SIZE + 10))
        # Display no path message
        if no_path_message:
            self.screen.blit(no_path_message, (WINDOW_SIZE // 2 - 50, WINDOW_SIZE // 2))
        pygame.display.flip()

    def check_button_click(self, pos):
        for button in self.buttons:
            if button["rect"].collidepoint(pos):
                if "mode" in button:
                    return button["mode"], None, None
                if "heuristic" in button:
                    return None, button["heuristic"], button["heuristic_name"]
        return None, None, None