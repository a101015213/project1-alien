import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():

    pygame.init()                             ##启动一个项目
    ai_settings=Settings()                    ##调用类Settings
    screen = pygame.display.set_mode(                    ##返回了一个什么值？
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')   ##定义名称

    ship=Ship(ai_settings,screen)     ##创建一个名为ship的Ship实例，一艘飞船

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()           ##运行游戏