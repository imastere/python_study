import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class for manage bullet of ship """

    def __init__(self, ai_settings, screen, ship):
        """create a bullet in ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # creat a rectangle in (0,0) to express the bullet
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store decimal to express bullet's position
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move up bullet"""

        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """draw a bullet in screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
