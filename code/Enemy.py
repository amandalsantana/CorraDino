

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:  # Se sair da tela por baixo
           self.rect.top = 0

        # Movendo da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name] * 2