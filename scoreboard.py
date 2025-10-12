import pygame
from settings import WHITE, WINDOW_WIDTH


class Scoreboard:
    def __init__(self, font_size=36):
        """Initialize the scoreboard."""
        self.score = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.position = (10, 10)  # Top-left corner

    def draw(self, screen):
        """Draw the current score on the screen."""
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, self.position)

    def increment_score(self):
        """Increase the score by 1."""
        self.score += 1

    def reset_score(self):
        """Reset the score to 0."""
        self.score = 0

    def get_score(self):
        """Return the current score."""
        return self.score