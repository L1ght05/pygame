import pygame
from settings import BLOCK_SIZE, GREEN, UP, DOWN, LEFT, RIGHT, WINDOW_WIDTH, WINDOW_HEIGHT


class Snake:
    def __init__(self, start_x=WINDOW_WIDTH // 2, start_y=WINDOW_HEIGHT // 2):
        """Initialize the snake with a starting position."""
        self.body = [(start_x, start_y), (start_x - BLOCK_SIZE, start_y), (start_x - 2 * BLOCK_SIZE, start_y)]
        self.direction = RIGHT  # Initial direction
        self.grow = False  # Flag to indicate if snake should grow

    def draw(self, screen):
        """Draw the snake on the screen."""
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        """Update the snake's position based on its direction."""
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x * BLOCK_SIZE, head_y + dir_y * BLOCK_SIZE)

        # Screen wrapping: if snake goes off edge, wrap around
        new_head = (new_head[0] % WINDOW_WIDTH, new_head[1] % WINDOW_HEIGHT)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()  # Remove tail if not growing
        else:
            self.grow = False  # Reset grow flag

    def change_direction(self, new_direction):
        """Change the snake's direction, preventing reversal."""
        # Prevent the snake from reversing into itself
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow_snake(self):
        """Set flag to grow the snake on next move."""
        self.grow = True

    def check_self_collision(self):
        """Check if snake has collided with itself."""
        head = self.body[0]
        return head in self.body[1:]

    def get_head_position(self):
        """Return the position of the snake's head."""
        return self.body[0]