# snake.py
import pygame
from settings import GREEN, UP, DOWN, LEFT, RIGHT


class Snake:
    def __init__(self, start_x, start_y, block_size=20, offset=(0, 0), grid_size=(800, 600)):
        self.block_size = block_size
        self.offset_x, self.offset_y = offset
        self.grid_width, self.grid_height = grid_size

        # Initialize body on-grid
        self.body = [
            (start_x, start_y),
            (start_x - self.block_size, start_y),
            (start_x - 2 * self.block_size, start_y)
        ]
        self.direction = RIGHT
        self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen, GREEN,
                (segment[0], segment[1], self.block_size, self.block_size)
            )

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (
            head_x + dir_x * self.block_size,
            head_y + dir_y * self.block_size
        )

        # Wrap within grid bounds (offset-aware)
        rel_x = (new_head[0] - self.offset_x) % self.grid_width
        rel_y = (new_head[1] - self.offset_y) % self.grid_height
        new_head = (self.offset_x + rel_x, self.offset_y + rel_y)

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        # Prevent 180° turn
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def get_head_position(self):
        return self.body[0]