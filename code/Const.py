# C
import pygame


C_ORANGE = (230, 115, 0)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_BROWN = (98, 49, 0)
C_CYAN = (0, 128, 128)

# E

ENTITY_DAMAGE = {
    'L1BG0' : 0,
    'L1BG1' : 0,
    'L1BG2' : 0,
    'L1BG3' : 0,
    'L1BG4' : 0,
    'L1BG5' : 0,
    'Jogador': 10,
    'enemy2': 10    
}

ENTITY_HEALTH = {
    'L1BG0' : 999,
    'L1BG1' : 999,
    'L1BG2' : 999,
    'L1BG3' : 999,
    'L1BG4' : 999,
    'L1BG5' : 999,
    'Jogador': 30,
    'enemy2': 10
}

ENTITY_SPEED = {
    'L1BG0' : 0,
    'L1BG1' : 1,
    'L1BG2' : 2,
    'L1BG3' : 3,
    'L1BG4' : 4,
    'L1BG5' : 5,
    'Jogador': 3,
    'enemy2': 5
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = ('COMO JOGAR',
               'JOGAR',
               'SAIR')

# T
TIMEOUT_STEP = 100

# W
WIN_WIDTH = 493
WIN_HEIGHT = 417
