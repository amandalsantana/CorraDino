#-*- coding: utf-8 -*-

import random
import pygame
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'L1BG':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'L1BG{i}', (0,0)))
                    list_bg.append(Background(f'L1BG{i}', (WIN_WIDTH,0)))
                return list_bg
            case 'Jogador':
            #case 'Run':
                return Player('Jogador', (1, 200))
                # list_pl = []
                # for i in range(1, 5):
                #     list_pl.append(Player(f'Run ({i})', (1,200)))
                # return list_pl
            case 'enemy2':  
                #return Enemy('Player1', (random.randint(0, WIN_HEIGHT), WIN_WIDTH + 10)) 
                return Enemy('enemy2', (random.randint(0, WIN_WIDTH),0))           
