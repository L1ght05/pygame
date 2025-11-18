# settings.py
import pygame

pygame.init()
info = pygame.display.Info()

# Default windowed size
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Game states
STATE_START = "start"
STATE_PLAYING = "playing"
STATE_GAME_OVER = "game_over"

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Default gameplay config (will be overridden per-session)
FPS = 10