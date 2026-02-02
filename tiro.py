import pygame

class Tiro():
    def __init__(self, x, y, largura, altura, velocidade, index, frame):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.index = index
        self.frame = frame
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

   
    def desenhar(self, tela):
        self.tiro_frame = self.frame[int(self.index)]
        self.tiro_frame_ampliado = pygame.transform.scale(self.tiro_frame, (self.largura, self.altura))
        tela.blit(self.tiro_frame_ampliado, (self.x, self.y))
        self.index += 0.15
        if self.index >= len(self.frame):
            self.index = 0
        self.y -= self.velocidade
        self.rect.y = self.y


class Especial():
    def __init__(self, x, y, largura, altura, velocidade, index, frame):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.index = index
        self.frame = frame
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    
    def desenhar(self, tela):
        if self.frame:
            self.especial_frame = self.frame[int(self.index)]
            self.especial_frame_ampliado = pygame.transform.scale(self.especial_frame, (self.largura, self.altura))
            tela.blit(self.especial_frame_ampliado, (self.x, self.y))
            self.index += 0.15
            if self.index >= len(self.frame):
                self.index = 0
        self.y -= self.velocidade
        self.rect.y = self.y