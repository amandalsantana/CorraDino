# C
import pygame


COLOR_ORANGE = (230, 115, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# E

ENTITY_HEALTH = {
    'L1BG0' : 999,
    'L1BG1' : 999,
    'L1BG2' : 999,
    'L1BG3' : 999,
    'L1BG4' : 999,
    'L1BG5' : 999,
    'Jogador': 300,
    'enemy2': 50
}

ENTITY_SPEED = {
    'L1BG0' : 0,
    'L1BG1' : 1,
    'L1BG2' : 2,
    'L1BG3' : 3,
    'L1BG4' : 4,
    'L1BG5' : 5,
    'Jogador': 3,
    'enemy2': 3
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NOVO JOGO 1P',
               'NOVO JOGO 2P - COOPERATIVO',
               'NOVO JOGO 2P - COMPETITIVO',
               'PONTUACAO',
               'SAIR')

# W
WIN_WIDTH = 493
WIN_HEIGHT = 417
