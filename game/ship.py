import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        '''init the ship and set its position'''

        self.screen = screen

        self.ai_settings = ai_settings

        # load image of shipo and get the bounding rectangle
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set new ship to the center bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float value to ship's attribute center
        self.center = float(self.rect.centerx)

        # symbol of moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """according to symbol of moving to adjust the position of ship"""
        # update value of centerx instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # according to slef.centerx update object for rect
        self.rect.centerx = self.center

    def blitme(self):
        """draw ship in specified postion"""
        self.screen.blit(self.image, self.rect)
