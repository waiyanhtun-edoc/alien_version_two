
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class manage the bullet"""
    def __init__(self,game_screen):
        """Initialize the bullet settings"""
        super().__init__()
        self.screen = game_screen.screen
        self.settings = game_screen.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = game_screen.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)