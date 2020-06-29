import sys

import pygame


def check_events(ship):
    """response key and click for mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def check_keydown_events(event, ship):
    """response keydown"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        print("right")
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        print("left")


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """refresh image for screen and shift to new screen """
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # display last screen and make it to be visible
    pygame.display.flip()
