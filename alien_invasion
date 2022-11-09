#!/usr/bin/env python3
import sys
import pygame
from setting import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.simo = Settings()

        self.screen = pygame.display.set_mode((self.simo.screen_width, self.simo.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse event
            self.check_events()
            self.update_screen()

    def update_screen(self):
        """Update images on teh screen, and flip to the new screen."""

        self.screen.fill(self.simo.bg_color)
        self.ship.blitme()
        # Make teh most recently drawn screen
        pygame.display.flip()



    def check_events(self):
        """responde to keypresses and mouse events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    # Make a game instance, and run the game
    my_game = AlienInvasion()
    my_game.run_game()
~                                                                                            
~                                     
