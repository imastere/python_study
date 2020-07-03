import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """express a alien class"""

    def __init__(self, ai_settings, screen):
        """init alien and setting the initial """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of alien,and set the rect attribute
        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien initial position is nearby upper left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store every precise position
        self.x = float(self.rect.x)

    def blitme(self):
        """ draw a alien in specified position"""
        self.screen.blit(self.image, self.rect)


    def check_edgs(self):
        """If the alien is at the edge of the screen, return to True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <=0:
            return True

    def update(self):
        """alien move towards the left """
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x


