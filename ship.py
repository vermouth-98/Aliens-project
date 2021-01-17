import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """ Initialize the ship and set its starting position """
        super(Ship, self).__init__()
        self.screen =screen
        self.ai_settings = ai_settings
        #load the ship image and get its rect
        self.image = pygame.image.load('spaceship.bmp') # to load image
        self.rect = self.image.get_rect()# make to image like rectage instead of shaped ship
        self.screen_rect = screen.get_rect()
        
        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        elif self.moving_left and self.rect.left> 0:
            self.center-= self.ai_settings.ship_speed

        self.rect.centerx = self.center
    def blitme(self):
        """ Draw the ship at its current location """
        
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        ''' respond the ship on the center of screen '''
        self.center = self.screen_rect.centerx
