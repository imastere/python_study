import pygame


class Ship():
    def __init__(self, screen):

        '''init the ship and set its position'''

        self.screen = screen
        # load image of shipo and get the bounding rectangle
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set new ship to the center bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw ship in specified postion"""
        self.screen.blit(self.image, self.rect)
