import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, FPS
from snake import Snake


def run_stage1():
    """Stage 1: Display static snake on board."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game - Stage 1: Static Snake")
    clock = pygame.time.Clock()

    # Create a static snake (no movement)
    snake = Snake()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BLACK)

        # Draw static snake
        snake.draw(screen)

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run_stage1()