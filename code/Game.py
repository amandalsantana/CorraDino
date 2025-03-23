#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame

from code.End import End
from code.Instruction import Instruction
from code.Level import Level
from code.Menu import Menu
from code.Const import C_ORANGE, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from pygame import Surface, Rect
from pygame.font import Font

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
 
            if menu_return == MENU_OPTION[0]:
                inst = Instruction(self.window)
                inst.run()
            elif menu_return in (MENU_OPTION[1]):
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
                if level_return:
                   end = End(self.window, 1)
                   end.run() 
                else:
                   end = End(self.window, 2)
                   end.run()                
            elif menu_return == MENU_OPTION[2]:
                pygame.quit() 
                quit()
            else:
                pass

    def begin_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='arial', size=text_size, bold = pygame.font.Font.bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
