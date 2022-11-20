#!/usr/bin/env python3
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class for managing bullets fired form the ship"""

    def __init__(self,my_game1):
        """ Creat a bullet object at the ship's current position."""
        super().__init__()
        self.screen = my_game1.screen
        self.simo = my_game1.simo
        self.color = self.simo.bullet_color

        #Create a bullet rect at (0,0) and then set corrent position. 
        self.rect = pygame.Rect(0, 0, self.simo.bullet_width, self.simo.bullet_height)
        self.rect.midtop = my_game1.ship.rect.midtop

        # Store teh bullet's position as a decimal value.
        self.y = float(self.rect.y)


    def update(self):
        """Move te bullet up the screen."""
        # Update the decimal position of hte bullet.

        self.y -= self.simo.bullet_speed
        # Update the rect position.
        self.rect.y = self.y 

    def draw_bullet(self):
        """ Drawing the b8ullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
