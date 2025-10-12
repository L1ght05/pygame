import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, FPS, UP, DOWN, LEFT, RIGHT
from snake import Snake
from food import Food


def run_stage3():
    """Stage 3: Add food and growth."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game - Stage 3: Food and Growth")
    clock = pygame.time.Clock()

    # Create snake and food
    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        # Move snake
        snake.move()

        # Check for food collision
        if food.check_collision(snake.get_head_position()):
            snake.grow_snake()
            food.respawn(snake.body)

        # Clear screen
        screen.fill(BLACK)

        # Draw snake and food
        snake.draw(screen)
        food.draw(screen)

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run_stage3()