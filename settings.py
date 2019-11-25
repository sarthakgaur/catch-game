class Settings():
    """A model for all the settings in the game"""

    def __init__(self):
        """Initialize all the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Catcher Settings
        self.catcher_speed = 2

        # Ball Settings
        self.ball_speed = 1
