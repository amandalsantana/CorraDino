
from code.Const import ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:  # Se sair da tela por baixo
           self.rect.top = 0

        # Movendo da direita para a esquerdaou da esquerda para a direita 
        self.rect.centerx -= (1.0 if self.direction == "right_to_left" else -1.0) * ENTITY_SPEED[self.name] * 1.5