# food.py
import random
import pygame
from settings import RED


class Food:
    def __init__(self, block_size=20, offset=(0, 0), grid_size=(800, 600)):
        self.block_size = block_size
        self.offset_x, self.offset_y = offset
        self.grid_width, self.grid_height = grid_size
        self.color = RED
        self.position = self.random_position()

    def random_position(self):
        max_x = self.grid_width // self.block_size
        max_y = self.grid_height // self.block_size
        x = random.randint(0, max_x - 1) * self.block_size
        y = random.randint(0, max_y - 1) * self.block_size
        return (self.offset_x + x, self.offset_y + y)

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color,
            (*self.position, self.block_size, self.block_size)
        )

    def respawn(self, snake_body):
        # Try up to 100 times to find free spot
        for _ in range(100):
            pos = self.random_position()
            if pos not in snake_body:
                self.position = pos
                return
        # Fallback: keep current (extremely rare)

    def check_collision(self, snake_head):
        return self.position == snake_head