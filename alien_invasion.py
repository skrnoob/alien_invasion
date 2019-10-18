import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings ,screen)
    bullets = Group()
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监听事件，摆循环最前
        gf.check_events(ship, bullets,ai_settings,screen)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()