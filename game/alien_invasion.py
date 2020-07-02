import sys
import pygame
import game.game_functions as gf
from game.settings import Settings
from game.ship import Ship
from game.alien import Alien
from pygame.sprite import Group


def run_game():
    # init game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a new ship
    ship = Ship(ai_settings, screen)

    aliens = Group()

    # create alien's group
    gf.create_fleet(ai_settings, screen, ship,aliens)

    # create a group to store the bullet
    bullets = Group()

    # start game's main circulation
    while True:
        # listen mouse and keyboard
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)
        # print(len(bullets))

        # redraw screen every circulation
        # let last screen be visible
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
