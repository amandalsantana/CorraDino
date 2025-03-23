#-*- coding: utf-8 -*-

import sys
from tkinter.font import Font
import pygame
from code.EntityMediator import EntityMediator
from code.Const import C_BROWN, C_CYAN, C_ORANGE, C_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, TIMEOUT_STEP, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window =  window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('L1BG'))
        self.entity_list.append(EntityFactory.get_entity('Jogador'))
        self.timeout = 45000 # 25 segundos
        pygame.time.set_timer(EVENT_ENEMY, 2000)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        pygame.mixer_music.load('./asset/jogo.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        frame_delay = 100  # Tempo em milissegundos para trocar o frame
        last_update = pygame.time.get_ticks()

        while True:
            clock.tick(50)
            now = pygame.time.get_ticks()
            
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if ent.name == 'Jogador':
                    self.level_text(14, f'Jogador - Health: {ent.health}', C_ORANGE, (10, 25))
                    if now - last_update > frame_delay:
                        last_update = now
                        ent.update_animation()    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('enemy2'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                if self.timeout <= 0:
                    for ent in self.entity_list:
                        if ent.name == 'Jogador' and ent.health > 0:
                           return True

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10,5))
            pygame.display.flip()
            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            for ent in self.entity_list:
                if ent.name == 'Jogador' and ent.health <= 0:
                   return False
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='arial', size=text_size, bold = pygame.font.Font.bold)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)