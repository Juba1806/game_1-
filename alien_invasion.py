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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)



    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse event
            self.check_events()
            self.ship.update()
            self.update_screen()

            

    def update_screen(self):
        """Update images on teh screen, and flip to the new screen."""

        self.screen.fill(self.simo.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen
        pygame.display.flip()



    def check_events(self):
        """responde to keypresses and mouse events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_KEYDOWN(event)

            elif event.type == pygame.KEYUP:
                self.check_KEYUP(event)
                
                
    def check_KEYDOWN(self, event):
        """Check when the player press a bottom  """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()


    def check_KEYUP(self,event):
        """check the when the player let go the bottoms"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == "__main__":
    # Make a game instance, and run the game
    my_game = AlienInvasion()
    my_game.run_game()
                                     
