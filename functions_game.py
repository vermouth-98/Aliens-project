from scoreboard import Scoreboard
import sys

import pygame
from pygame.constants import KEYDOWN, KEYUP, MOUSEBUTTONDOWN

from bullet import Bullet
from alien import Alien
from time import sleep
from save_file import *
def fire_bullets(ai_settings,screen,ship,bullets,bullet_sound):
    """ create bullets """
    if len(bullets)<ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        bullet_sound.play()

def get_number_alienx(ai_settings, alien):
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width- 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,number_aliens_x,aliens, number_rows):
    #create an alien and place it in the row
    alien= Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width +2*alien_width*number_aliens_x
    alien.rect.x = alien.x
    alien.rect.y = alien_height+2*alien_height*number_rows
    aliens.add(alien)


def get_number_rows(ai_settings, alien,ship):
    alien_height = alien.rect.height
    available_space_y = ai_settings.screen_height - 3*alien_height - ship.rect.height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_fleet(ai_settings, screen, aliens,ship):
    """ create a full fleet of aliens. """
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_alienx(ai_settings,alien)
    number_rows = get_number_rows(ai_settings,alien, ship )
    #create the first row of aliens
    for row_number in range(number_rows):
        for number_alien in range(number_aliens_x):
            #create an alien and place it in the row
            create_alien(ai_settings,screen,number_alien, aliens,row_number)

def check_fleet_edges(ai_settings, aliens):
    """ Respond appropriately if any aliens have reached an edge """
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *=-1

def check_key_down(event,ai_settings,screen,stats,aliens, ship,bullets,score_board,bullet_sound):
    """ respond to key down  """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets,bullet_sound)
    elif event.key == pygame.K_p and not stats.game_active:
        pygame.mouse.set_visible(False)
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active =True
        #reset level and score
        score_board.prep_level()
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_ship()
        #hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        clear_screen(ai_settings, screen, aliens, ship, bullets)

def check_play_button(ai_settings,screen,stats,aliens,ship,bullets
                        ,play_button, mouse_x, mouse_y,score_board):
    ''' Start a new game with player clicks play '''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #reset the game settings
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active =True
        #reset level and score
        score_board.prep_level()
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_ship()
        #hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        clear_screen(ai_settings, screen, aliens, ship, bullets)
        

def check_key_up (event,ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key== pygame.K_LEFT:
        ship.moving_left = False
    

def check_event(ai_settings, screen,stats,aliens,ship,bullets,play_button,score_board,bullet_sound):
    """ respond to keypresses and mouse events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_file(stats.high_score,ai_settings)
            sys.exit()
        elif event.type == KEYDOWN:
            check_key_down(event,ai_settings,screen,stats,aliens, ship, bullets,score_board,bullet_sound)
            if event.key == pygame.K_ESCAPE:
                write_file(stats.high_score,ai_settings)
                sys.exit()
        elif event.type ==KEYUP:
            check_key_up(event,ai_settings,screen, ship,bullets)
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,aliens,ship,
                                bullets,play_button, mouse_x, mouse_y,score_board)


def update_screen(ai_settings , screen,stats, ship, bullets, aliens,play_button,score_board):
    """ Update images on the screen and flip to the new screen """
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.background_color)  
    score_board.show_score()
    if stats.game_active:
        #redraw all bullets behind ship and alien
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        #redraw ship    
        ship.blitme()
        #redraw alien
        aliens.draw(screen)
    else:
        #redraw button
        play_button.draw_button()
    pygame.display.flip()

def check_collision_bullet_aliens (ai_settings , screen,stats, ship, bullets, aliens,score_board):
    """ respond to bullet- aliens collisions"""
    collisions = pygame.sprite.groupcollide(bullets,aliens,True, True)
    if collisions:
        for value_aliens in collisions.values():
            stats.score += ai_settings.alien_points
            score_board.prep_score()
        check_high_score(stats,score_board)
    if len(aliens)== 0:
        #destroy existing bullets and create new fleet
        update_level(ai_settings,screen, stats,aliens,ship, bullets,score_board)

def update_level(ai_settings, screen,stats, aliens, ship,bullets,score_board):
    bullets.empty()
    ai_settings.increase_speed()
    #increase level
    stats.level+=1
    score_board.prep_level()
    create_fleet(ai_settings,screen,aliens,ship)

def update_bullets(ai_settings,screen, ship,stats, bullets, aliens,score_board):
    bullets.update()
    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_collision_bullet_aliens(ai_settings, screen,stats,ship,bullets,aliens,score_board)

def ship_hit(ai_settings,screen, ship, aliens, bullets, stats,score_board):
    ''' respond to ship being hit by alien '''
    #Decrement ships left
    if stats.ship_left >0:
        stats.ship_left -=1
        #empty the list of aliens and bullets
        score_board.prep_ship()
        clear_screen(ai_settings,screen,aliens,ship,bullets)
        #pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_collision_aliens_ship(ai_settings,screen, ship, aliens,bullets, stats,score_board):
    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,screen,ship,aliens,bullets, stats,score_board)
def check_aliens_bottom(ai_settings,screen, ship, aliens,bullets, stats):

    screen_rect = screen.get_rect()# get information of screen
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen, ship, aliens, bullets,stats)
            break

def update_aliens(ai_settings,screen, ship,aliens,bullets, stats,score_board):
    """ Update the posions of all aliens in the fleet """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #look for alien_ship collision
    check_collision_aliens_ship(ai_settings, screen, ship, aliens, bullets,stats,score_board)
    check_aliens_bottom(ai_settings, screen, ship, aliens, bullets,stats)

def clear_screen (ai_settings,screen, aliens, ship,bullets):
    aliens.empty()
    bullets.empty()
    #create a new fleet and center the ship
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()

def check_high_score(stats, score_board):
    if stats.score> stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()