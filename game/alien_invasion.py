import sys
import pygame

from game.settings import Settings
from game.ship import Ship


def run_game():
    # init game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a new ship
    ship = Ship(screen)

    # start game's main circulation
    while True:
        # redraw screen every circulation
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # listen mouse and keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # let last screen be visible
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
