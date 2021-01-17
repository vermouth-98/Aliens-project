import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet """
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and set its starting position
        self.image = pygame.image.load("UFO.bmp")
        self.rect = self.image.get_rect()
        
        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        
        #store exact position of alien
        self.x = float(self.rect.x)
    
    def check_edge(self):
        """ Return true if alien is at edge of screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left<= 0:
            return True          

    def update(self):
            #moving aliens
        self.x += self.ai_settings.alien_speed*self.ai_settings.fleet_direction
        self.rect.x = self.x

