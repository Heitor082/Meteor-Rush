import pygame

class Inimigo():
    def __init__(self, x, y, largura, altura, velocidade, index, frame):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.index = index
        self.frame = frame
        self.vivo = True
        self.rect = pygame.Rect(self.x + 75, self.y + 75, self.largura - 150, self.altura - 150)
        self.collision_rect = pygame.Rect(self.x + 137.5, self.y + 137.5, 25, 25)
        self.animacao_morte_concluida = False

    def desenhar(self, tela):
        if self.vivo:
            self.inimigo_frame = self.frame[0]
            self.inimigo_frame_ampliado = pygame.transform.scale(self.inimigo_frame, (self.largura, self.altura))
            tela.blit(self.inimigo_frame_ampliado, (self.x, self.y))
        else:
            if not self.animacao_morte_concluida:
                self.inimigo_morrendo_frame = self.frame[int(self.index)]
                self.inimigo_morrendo_frame_ampliado = pygame.transform.scale(self.inimigo_morrendo_frame, (self.largura, self.altura))
                tela.blit(self.inimigo_morrendo_frame_ampliado, (self.x, self.y))
                self.index += 0.15
                if self.index >= len(self.frame):
                    self.animacao_morte_concluida = True

    def mover(self, jogador):
        if self.vivo:
            self.y += self.velocidade
            self.rect.x = self.x + 75
            self.rect.y = self.y + 75
            self.collision_rect.x = self.x + 137.5
            self.collision_rect.y = self.y + 137.5
            if self.y + self.altura > 675 and not jogador.em_easter_egg:
                jogador.vida -= 1
                self.vivo = False