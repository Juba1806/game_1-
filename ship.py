#!/usr/bin/env python3
import pygame

class Ship:
    """A xlass to manage the ship."""

    def __init__(self, my_game1):
        """Intialize the sip and set its starting positiong."""
        self.screen = my_game1.screen
        self.screen_rect = my_game1.screen.get_rect()

        # Load the ship image and get its rect
       # self.image = pygame.image.load("rocket_ship.bmp")

        image = pygame.image.load("rocket_ship.bmp")
        self.image = pygame.transform.scale(image,(200,160))
        self.rect = self.image.get_rect()

        # Start each new shit at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
~                                                                                            
~                                                                                            
~                                                                                            
~                                                          
