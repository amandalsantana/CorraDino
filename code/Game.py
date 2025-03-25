
import pygame

from code.End import End
from code.Instruction import Instruction
from code.Level import Level
from code.Menu import Menu
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH


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
