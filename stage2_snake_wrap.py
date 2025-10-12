import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, FPS, UP, DOWN, LEFT, RIGHT
from snake import Snake


def run_stage2():
    """Stage 2: Snake movement with screen wrapping."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game - Stage 2: Movement with Wrapping")
    clock = pygame.time.Clock()

    # Create snake
    snake = Snake()

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

        # Clear screen
        screen.fill(BLACK)

        # Draw snake
        snake.draw(screen)

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run_stage2()