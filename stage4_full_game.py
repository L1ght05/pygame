import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, FPS, UP, DOWN, LEFT, RIGHT
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def run_stage4():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game - Stage 4")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    start_sound = pygame.mixer.Sound("pygame/assets/game-start-317318.mp3")
    pickup_sound = pygame.mixer.Sound("pygame/assets/coin_c_02-102844.mp3")
    death_sound = pygame.mixer.Sound("pygame/assets/dead-sound-221863.mp3")

    start_sound.set_volume(0.7)
    pickup_sound.set_volume(0.6)
    death_sound.set_volume(0.8)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game_over = False

    start_sound.play()

    def reset_game():
        nonlocal snake, food, scoreboard, game_over
        snake = Snake()
        food = Food()
        scoreboard.reset_score()
        game_over = False
        start_sound.play()

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
            snake.move()
            if food.check_collision(snake.get_head_position()):
                snake.grow_snake()
                food.respawn(snake.body)
                scoreboard.increment_score()
                pickup_sound.play()
            if snake.check_self_collision():
                game_over = True
                death_sound.play()

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        scoreboard.draw(screen)

        if game_over:
            game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(game_over_text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    run_stage4()
