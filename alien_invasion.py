from hashlib import new
import sys
import pygame
from settings import Settings
from ship import Ship
from background import Background
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialie the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        #set the game screen size
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.background = Background(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self.ship.update()
            self._update_buttet()
            self._update_screen()
            
            # print (len(self.bullets))
            
    def _update_buttet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

            
    def _check_event(self):
        """Check the game event """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keypress(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
                
    def _check_keypress(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _fire_bullet(self):
        """Add new bullet to group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _check_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    

    def _update_screen(self):
        """Update the screen everything"""
        self.background.blitBack()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()