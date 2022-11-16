#!/usr/bin/env python3
import pygame

class Ship:
    """A xlass to manage the ship."""

    def __init__(self, my_game1):
        """Intialize the sip and set its starting positiong."""
        self.screen = my_game1.screen
        self.simo = my_game1.simo
        self.screen_rect = my_game1.screen.get_rect()

        # Load the ship image and get its rect
       # self.image = pygame.image.load("rocket_ship.bmp")

        image = pygame.image.load("rocket_ship.bmp")
        self.image = pygame.transform.scale(image,(200,160))
        self.rect = self.image.get_rect()

        # Start each new shit at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Moving the flag 
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """UPdate the ship's position based on the flag movement """
        if self.moving_right and self.rect.right < self.screen_rect.right + 80 :
            self.x += self.simo.ship_speed
        if self.moving_left and self.rect.left > -80:
            self.x -= self.simo.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

        
