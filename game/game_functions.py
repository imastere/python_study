import sys

import pygame
from game.bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """response key and click for mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """response keydown"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:

        # create a bullet,and add to bullets's Group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        print("--- ")


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """refresh image for screen and shift to new screen """
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()


    ship.blitme()

    # display last screen and make it to be visible
    pygame.display.flip()
