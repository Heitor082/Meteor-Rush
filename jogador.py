import pygame

class Jogador():
    def __init__(self, x, y, largura, altura, velocidade, index, frame):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.index = index
        self.frame = frame
        self.atirando = False
        self.tela_3 = False

    def desenhar(self, tela):
        self.jogador_atirando_frame = self.frame[int(self.index)]
        self.jogador_atirando_frame_ampliado = pygame.transform.scale(self.jogador_atirando_frame, (self.largura, self.altura))
        tela.blit(self.jogador_atirando_frame_ampliado, (self.x, self.y))

    def andar(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[pygame.K_w]:
            self.y -= self.velocidade
        if self.teclas[pygame.K_s]:
            self.y += self.velocidade
        if self.teclas[pygame.K_a]:
            self.x -= self.velocidade
        if self.teclas[pygame.K_d]:
            self.x += self.velocidade
        if self.x >= 1100:
            self.x = 1100
        if self.x <= -200:
            if self.y == -200:
                pass
            else:
                self.x = -200
        if self.y >= 525:
            self.y = 525
        if self.y <= -200:
            self.y = -200
        if self.x == -5000 and self.y == - 200:
            self.tela_3 = True
        

    def atirar(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[pygame.K_SPACE]:
            self.index += 0.15
            if self.index > 6:
                self.index = 0
        else:
            self.index = 0
