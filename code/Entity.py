
from abc import ABC, abstractmethod
import random
import pygame
from code.Const import ENTITY_DAMAGE, ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

        if self.name == "Jogador":
            # Carrega várias imagens para a animação do jogador
            self.frames = [
                pygame.image.load(f'./asset/Run (1).png').convert_alpha(),
                pygame.image.load(f'./asset/Run (2).png').convert_alpha(),
                pygame.image.load(f'./asset/Run (3).png').convert_alpha(),
                pygame.image.load(f'./asset/Run (4).png').convert_alpha(),
                pygame.image.load(f'./asset/Run (5).png').convert_alpha(),
                pygame.image.load(f'./asset/Run (6).png').convert_alpha(),
                pygame.image.load(f'./asset/Run (7).png').convert_alpha(),
                pygame.image.load(f'./asset/Run (8).png').convert_alpha()
            ]
            self.frame_index = 0
            self.surf = self.frames[self.frame_index]
        else:
            # Apenas uma imagem para inimigo e background
            self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) 
        
        if self.name == 'Inimigo':
            self.direction = random.choice(["left_to_right", "right_to_left"])
            if self.direction == 'left_to_right':
                self.surf = pygame.transform.flip(self.surf, True, False)

    def update_animation(self):
        # Atualiza a animação do jogador trocando de frame.
        if self.name == "Jogador":
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]


    @abstractmethod
    def move(self):
        pass

