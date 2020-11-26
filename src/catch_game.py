import pygame
import game_functions as gf
from pygame.sprite import Group
from catcher import Catcher
from settings import Settings
from game_stats import Stats

pygame.init()
# Making an instance of settings
game_settings = Settings()

# Making an instance of Stats
game_stats = Stats()

# create screen and background color
screen = pygame.display.set_mode((game_settings.screen_width,
        game_settings.screen_height))
bg_color = game_settings.bg_color

# Make a new ball
balls = Group()

# Make a catcher
catcher = Catcher(screen, game_settings)

def run_game():
    """This function runs the game."""

    # This game runs inside this loop.
    while True:
        gf.check_events(catcher)
        if game_stats.game_active:
            gf.update_screen(screen, bg_color, balls, catcher, game_settings, game_stats)

run_game()