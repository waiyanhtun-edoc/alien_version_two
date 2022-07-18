import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self,game_screen):
        """Initialize the ship and set its starting position."""
        #set thet game_screen background with rect
        self.screen = game_screen.screen
        self.settings = game_screen.settings
        self.screen_rect = self.screen.get_rect()

        #set the ship image and ship position with rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #set each new ship at the bottom of the game_scree
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        """Moving the ship left and right """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
