class Settings:
    """A Class to store all settings for Alen Invasion"""

    def __init__(self):
        """"Initialize the game's settings."""
        #ship settings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = (255,255,255)
        self.bullet_allowed = 5

        