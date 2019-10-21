import pygame
import sys
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ship,bullets,ai_settings,screen):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:

        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship,bullets,ai_settings,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,bullets,ai_settings,screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = (ai_settings.screen_height - ( 3 * alien_height ) -  ship_height)
    number_rows = int( available_space_y / ( 2 * alien_height ) )
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number_x, number_rows):

    for row_number in range(number_rows):
        for alien_number in range(alien_number_x):
            alien = Alien(ai_settings, screen)
            alien_width = alien.rect.width
            alien.x = alien_width + alien_width * 2 *alien_number
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            alien.rect.x = alien.x
            aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    alien_number_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)

    create_alien(ai_settings,screen,aliens,alien_number_x, number_rows)

def update_screen(ai_settings,screen,ship,bullets,aliens):
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    
    aliens.draw(screen)
    
    # 让最近绘制的屏幕可见，摆循环最后
    pygame.display.flip()