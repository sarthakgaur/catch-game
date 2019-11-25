import pygame

class Catcher():
    """Create a model of the catcher."""

    def __init__(self, screen, game_settings):
        """Initialize all the cather attributes."""

        # Load the image and get its rect
        self.image = pygame.image.load('images/catcher.jpg')
        self.rect = self.image.get_rect()

        # Get the screen and its rect
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Set catcher's starting point
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        # Setting movement flags
        self.moving_right = False
        self.moving_left = False

        # Making a game settings attribute
        self.game_settings = game_settings
    
    def move_him(self):
        """Moves the catcher if flag is True."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.game_settings.catcher_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.game_settings.catcher_speed
    
    def blit_me(self):
        """Display the image"""
        self.screen.blit(self.image, self.rect)