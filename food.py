import random
import pygame
from settings import BLOCK_SIZE, RED, WINDOW_WIDTH, WINDOW_HEIGHT


class Food:
    def __init__(self):
        """Initialize food at a random position."""
        self.position = self.random_position()
        self.color = RED

    def random_position(self):
        """Generate a random position for food on the grid."""
        x = random.randint(0, (WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return (x, y)

    def draw(self, screen):
        """Draw the food on the screen."""
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    def respawn(self, snake_body):
        """Respawn food in a new random location, avoiding snake body."""
        while True:
            new_position = self.random_position()
            if new_position not in snake_body:
                self.position = new_position
                break

    def check_collision(self, snake_head):
        """Check if snake head collides with food."""
        return self.position == snake_head