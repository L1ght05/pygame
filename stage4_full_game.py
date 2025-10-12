import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, FPS, UP, DOWN, LEFT, RIGHT
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def run_stage4():
    """Stage 4: Full game with score, self-collision, and restart."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game - Stage 4: Full Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    # Initialize game objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game_over = False

    def reset_game():
        nonlocal snake, food, scoreboard, game_over
        snake = Snake()
        food = Food()
        scoreboard.reset_score()
        game_over = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        reset_game()
                else:
                    if event.key == pygame.K_UP:
                        snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(RIGHT)

        if not game_over:
            # Move snake
            snake.move()

            # Check for food collision
            if food.check_collision(snake.get_head_position()):
                snake.grow_snake()
                food.respawn(snake.body)
                scoreboard.increment_score()

            # Check for self-collision
            if snake.check_self_collision():
                game_over = True

        # Clear screen
        screen.fill(BLACK)

        # Draw game objects
        snake.draw(screen)
        food.draw(screen)
        scoreboard.draw(screen)

        # Draw game over screen
        if game_over:
            game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(game_over_text, text_rect)

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run_stage4()