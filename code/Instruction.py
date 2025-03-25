import pygame

from code.Const import C_ORANGE, C_WHITE, WIN_WIDTH
import pygame.image
from pygame import K_ESCAPE, Surface, Rect
from pygame.font import Font


class Instruction:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Instrucao.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.inst_text(50, "Como", C_ORANGE, ((WIN_WIDTH / 2), 90))
            self.inst_text(50, "jogar", C_ORANGE, ((WIN_WIDTH / 2), 130))
            self.inst_text(20, "O objetivo do jogo é salvar o dinossauro", C_WHITE, (250, 180))
            self.inst_text(20, "dos meteoros que estão caindo na Terra.", C_WHITE, (250, 200))
            self.inst_text(20, "Utilize as teclas LEFT e RIGHT", C_WHITE, (250, 220))
            self.inst_text(20, "para evitar que o dino seja atingido.", C_WHITE, (250, 240))
            self.inst_text(20, "VOLTAR AO MENU: tecla ESC", C_ORANGE, (250, 280))
            
            pygame.display.flip()    

           # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                   if event.key == K_ESCAPE:
                      return

            
    def inst_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='arial', size=text_size, bold = pygame.font.Font.bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)