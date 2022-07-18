import pygame

class Background:
    """A class to manage the class"""

    def __init__(self,game_screen):
        """Initialize the game background"""
        
        self.screen = game_screen.screen
        self.screen_rect = self.screen.get_rect()


        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()

    def blitBack(self):
        self.screen.blit(self.image,self.rect)