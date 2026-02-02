import pygame

class Jogador():
    def __init__(self, x, y, largura, altura, velocidade, index, frame, paralisia_frames, especial_frames):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.index = index
        self.frame = frame
        self.paralisia_frames = paralisia_frames
        self.paralisia_index = 0
        self.especial_frames = especial_frames
        self.atirando = False
        self.tela_3 = False
        self.vida = 3
        self.pontuacao = 0
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.collision_rect = pygame.Rect(self.x + 125, self.y + 125, 50, 50)
        self.paralisado = False
        self.tempo_paralisia = 0
        self.em_easter_egg = False
        self.inimigos_derrotados = 0
        self.especial_pronto = False


    def desenhar(self, tela):
        self.jogador_atirando_frame = self.frame[int(self.index)]
        self.jogador_atirando_frame_ampliado = pygame.transform.scale(self.jogador_atirando_frame, (self.largura, self.altura))
        tela.blit(self.jogador_atirando_frame_ampliado, (self.x, self.y))
        
        if self.paralisado and self.paralisia_frames:
            self.paralisia_frame = self.paralisia_frames[int(self.paralisia_index)]
            self.paralisia_frame_ampliado = pygame.transform.scale(self.paralisia_frame, (self.largura, self.altura))
            tela.blit(self.paralisia_frame_ampliado, (self.x, self.y))
            self.paralisia_index += 0.15
            if self.paralisia_index >= len(self.paralisia_frames):
                self.paralisia_index = 0


    def andar(self):
        if self.paralisado:
            if pygame.time.get_ticks() > self.tempo_paralisia:
                self.paralisado = False
            else:
                return
        
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
            self.em_easter_egg = True
            if self.y == -200:
                pass
            else:
                self.x = -200
        else:
            self.em_easter_egg = False
        if self.y >= 525:
            self.y = 525
        if self.y <= -200:
            self.y = -200
        if self.x == -5000 and self.y == - 200:
            self.tela_3 = True
        
        self.rect.x = self.x
        self.rect.y = self.y
        self.collision_rect.x = self.x + 125
        self.collision_rect.y = self.y + 125
        
    def atirar(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[pygame.K_SPACE]:
            self.index += 0.15
            if self.index > 6:
                self.index = 0
            self.atirando = True    
        else:
            self.index = 0
            self.atirando = False
