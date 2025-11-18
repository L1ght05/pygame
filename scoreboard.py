# scoreboard.py
import pygame
from settings import WHITE


class Scoreboard:
    def __init__(self, font_size=36, position=(10, 10)):
        self.score = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.position = position

    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(text, self.position)

    def increment_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def get_score(self):
        return self.score