import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    """Create a model of a ball."""

    def __init__(self, screen, game_settings, game_stats):
        """Initialize all the ball attributes."""
        super().__init__()

        # Load the image and get its rect
        self.image = pygame.image.load('../images/ball.jpg')
        self.rect = self.image.get_rect()

        # Get the screen attribute
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Making a game_settings attribute
        self.game_settings = game_settings

        # Making a game_stats attribure
        self.game_stats = game_stats

        # Select the x and y coordinates
        self.rect.y = self.screen_rect.top
        self.rect.x = randint(0, self.screen_rect.right - self.rect.width)
    
    def drop(self):
        """Increase the position of the y coordinate"""
        self.rect.y += self.game_settings.ball_speed
    
    def below_screen(self):
        """Check if the ball is below the screen."""
        if self.rect.top >= self.screen_rect.bottom:
            self.game_stats.catch_fails_allowed -= 1
            return True
    
    def blit_me(self):
        """Display the image on the screen."""
        self.screen.blit(self.image, self.rect)
