import sys
import pygame
import game.game_functions as gf
from game.settings import Settings
from game.ship import Ship


def run_game():
    # init game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a new ship
    ship = Ship(ai_settings, screen)

    # start game's main circulation
    while True:
        # listen mouse and keyboard
        gf.check_events(ship)

        ship.update()

        # redraw screen every circulation
        # let last screen be visible
        gf.update_screen(ai_settings, screen, ship)





if __name__ == '__main__':
    run_game()

