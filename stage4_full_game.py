# stage4_full_game.py
import pygame
import os
from settings import (
    DEFAULT_WIDTH, DEFAULT_HEIGHT, BLACK, WHITE, GRAY, RED, GREEN,
    FPS, UP, DOWN, LEFT, RIGHT,
    STATE_START, STATE_PLAYING, STATE_GAME_OVER
)
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def load_sound(path, vol=0.6):
    class Dummy:
        def play(self): pass
        def set_volume(self, v): pass
    if os.path.exists(path):
        try:
            snd = pygame.mixer.Sound(path)
            snd.set_volume(vol)
            return snd
        except:
            pass
    return Dummy()


def run_game():
    pygame.init()
    pygame.mixer.init()

    # Initial window
    screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont(None, 64)
    font_med = pygame.font.SysFont(None, 36)
    font_small = pygame.font.SysFont(None, 24)

    # Load sounds (safe)
    start_snd = load_sound("assets/game-start-317318.mp3", 0.7)
    pickup_snd = load_sound("assets/coin_c_02-102844.mp3", 0.6)
    death_snd = load_sound("assets/dead-sound-221863.mp3", 0.8)

    # Game objects
    snake = None
    food = None
    scoreboard = None

    game_state = STATE_START
    fullscreen = False

    # Fullscreen dims (cached)
    info = pygame.display.Info()
    fs_w, fs_h = info.current_w, info.current_h

    def compute_layout():
        w, h = screen.get_size()
        # Target grid: ~40×30 blocks max, min block=15
        ideal_blocks_w, ideal_blocks_h = 40, 30
        block_w = max(15, w // ideal_blocks_w)
        block_h = max(15, h // ideal_blocks_h)
        block = min(block_w, block_h)  # square blocks

        grid_w = (w // block) * block
        grid_h = (h // block) * block
        ox = (w - grid_w) // 2
        oy = (h - grid_h) // 2
        return {
            'width': w, 'height': h,
            'grid_w': grid_w, 'grid_h': grid_h,
            'block': block,
            'ox': ox, 'oy': oy
        }

    layout = compute_layout()

    def reset_game():
        nonlocal snake, food, scoreboard, game_state
        layout = compute_layout()
        ox, oy = layout['ox'], layout['oy']
        gw, gh, block = layout['grid_w'], layout['grid_h'], layout['block']

        # Centered start
        start_x = ox + gw // 2
        start_y = oy + gh // 2
        # Snap to grid
        start_x = ox + ((start_x - ox) // block) * block
        start_y = oy + ((start_y - oy) // block) * block

        snake = Snake(start_x, start_y, block_size=block, offset=(ox, oy), grid_size=(gw, gh))
        food = Food(block_size=block, offset=(ox, oy), grid_size=(gw, gh))
        scoreboard = Scoreboard(position=(layout['ox'] + 10, layout['oy'] + 10))
        game_state = STATE_PLAYING
        start_snd.play()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE and not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                layout = compute_layout()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((fs_w, fs_h), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.RESIZABLE)
                    layout = compute_layout()

                elif game_state == STATE_START and event.key == pygame.K_SPACE:
                    reset_game()

                elif game_state == STATE_PLAYING:
                    if event.key == pygame.K_UP: snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN: snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT: snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT: snake.change_direction(RIGHT)

                elif game_state == STATE_GAME_OVER:
                    if event.key == pygame.K_r:
                        reset_game()
                    elif event.key == pygame.K_e:
                        running = False  # exit

        # --- Fullscreen button (□) ---
        w, h = screen.get_size()
        btn_size = 30
        btn_rect = pygame.Rect(w - btn_size - 10, 10, btn_size, btn_size)

        # Check mouse click
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_rect.collidepoint(mouse_pos):
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((fs_w, fs_h), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.RESIZABLE)
                    layout = compute_layout()

        # --- Game Logic ---
        if game_state == STATE_PLAYING and snake:
            snake.move()
            head = snake.get_head_position()
            if food.check_collision(head):
                snake.grow_snake()
                food.respawn(snake.body)
                scoreboard.increment_score()
                pickup_snd.play()
            if snake.check_self_collision():
                game_state = STATE_GAME_OVER
                death_snd.play()

        # --- Render ---
        screen.fill(BLACK)

        # Draw play area
        ox, oy = layout['ox'], layout['oy']
        gw, gh = layout['grid_w'], layout['grid_h']
        pygame.draw.rect(screen, (20, 20, 20), (ox, oy, gw, gh))

        # Draw game objects
        if snake: snake.draw(screen)
        if food: food.draw(screen)
        if scoreboard: scoreboard.draw(screen)

        # Fullscreen toggle button
        pygame.draw.rect(screen, GRAY, btn_rect, border_radius=4)
        pygame.draw.rect(screen, WHITE, btn_rect, 2, border_radius=4)
        inner = btn_rect.inflate(-12, -12)
        pygame.draw.rect(screen, WHITE, inner, 2)  # □

        # Screens
        if game_state == STATE_START:
            title = font_large.render("SNAKE", True, GREEN)
            sub = font_med.render("Classic Arcade Game", True, WHITE)
            start = font_med.render("Press SPACE to Start", True, GREEN)
            hint = font_small.render("F11 or □ to toggle Fullscreen", True, GRAY)
            screen.blit(title, title.get_rect(center=(w//2, h//2 - 80)))
            screen.blit(sub, sub.get_rect(center=(w//2, h//2 - 20)))
            screen.blit(start, start.get_rect(center=(w//2, h//2 + 40)))
            screen.blit(hint, hint.get_rect(center=(w//2, h//2 + 80)))

        elif game_state == STATE_GAME_OVER and scoreboard:
            over = font_large.render("GAME OVER", True, RED)
            final = font_med.render(f"Score: {scoreboard.get_score()}", True, WHITE)
            restart = font_med.render("Press R to Restart", True, GREEN)
            ex = font_med.render("Press E to Exit", True, WHITE)
            screen.blit(over, over.get_rect(center=(w//2, h//2 - 60)))
            screen.blit(final, final.get_rect(center=(w//2, h//2)))
            screen.blit(restart, restart.get_rect(center=(w//2, h//2 + 50)))
            screen.blit(ex, ex.get_rect(center=(w//2, h//2 + 90)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()