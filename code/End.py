import pygame

from code.Const import C_ORANGE, C_WHITE, WIN_WIDTH
import pygame.image
from pygame import K_ESCAPE, Surface, Rect
from pygame.font import Font


class End:
    def __init__(self, window, option):
        self.window = window
        self.surf = pygame.image.load('./asset/EndGame.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.option = option

    def run(self):
        pygame.mixer_music.load('./asset/menu.wav')
        pygame.mixer_music.play(-1)
        if self.option == 1:
            while True:
                # DRAW IMAGES
                # mensagem quando o jogador vence
                self.window.blit(source=self.surf, dest=self.rect)
                self.end_text(40, "PARABÉNS!!!", C_ORANGE, ((WIN_WIDTH / 2), 110))
                self.end_text(30, "Você salvou o dino!", C_WHITE, ((WIN_WIDTH / 2), 160))
                self.end_text(20, "VOLTAR AO MENU: tecla ESC", C_ORANGE, (250, 270))
                
                pygame.display.flip()    

            # Check for all events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  # Close Window
                        quit()  # end pygame
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            return
                        
        if self.option == 2:
            while True:
                # DRAW IMAGES
                # mensagem quando o jogador perde
                self.window.blit(source=self.surf, dest=self.rect)
                self.end_text(40, "VOCÊ PERDEU!!!", C_ORANGE, ((WIN_WIDTH / 2), 110))
                self.end_text(30, "O dino não foi salvo dessa vez...", C_WHITE, ((WIN_WIDTH / 2), 160))
                self.end_text(20, "VOLTAR AO MENU: tecla ESC", C_ORANGE, (250, 270))
                
                pygame.display.flip()    

            # Check for all events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  # Close Window
                        quit()  # end pygame
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            return

            
    def end_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='arial', size=text_size, bold = pygame.font.Font.bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)