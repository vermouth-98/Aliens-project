import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import functions_game as fg
from game_stats import GameStats
from button import Buttom
from scoreboard import Scoreboard


def run_game():
    """ Initialize game and create a screen object """
    pygame.init() # initialize background setting that Pygame needs to work properly

    """ initialize class settings """
    ai_settings = Settings()

    #create screen with width and height
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #A ship and the aliens is a surface,
                                                    # surface returned by display.set_mode()
    
    #set caption for screen
    pygame.display.set_caption("Alien Invasion")
    
    #make a ship
    ship = Ship(ai_settings, screen)
    
    # make group to store bullets in
    bullets = Group()
    
    #make a alien
    aliens = Group()
    #create a fleet of alien
    fg.create_fleet(ai_settings,screen,aliens,ship)  

    #create an instance to store game statistics
    stats = GameStats(ai_settings)

    #make buttom play
    play_button = Buttom(ai_settings,screen,"play")

    #ScoreBoard
    score_board = Scoreboard(ai_settings,screen,stats)
    #Start the main loop for the game.
    while True:
        # watch for keyboard and mouse events.
        fg.check_event(ai_settings, screen,stats,aliens,ship,bullets,play_button,score_board)
        if stats.game_active:
            ship.update()
            fg.update_bullets(ai_settings,screen,ship,stats, bullets,aliens,score_board)
            fg.update_aliens(ai_settings,screen, ship,aliens,bullets, stats,score_board)  
    #update images on the screen and flip to the new screen
        fg.update_screen(ai_settings,screen,stats,ship,bullets,aliens,play_button,score_board)    

run_game() 