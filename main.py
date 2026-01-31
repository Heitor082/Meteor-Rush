import pygame
from botao import Botao
from jogador import Jogador

pygame.init()

tela = pygame.display.set_mode((1200, 675))
pygame.display.set_caption("Meteor Rush")

relogio = pygame.time.Clock()

background_spritesheet = pygame.image.load("Assets/background/background.png").convert_alpha()
background_frames = []
for i in range(9):
    background_frame = background_spritesheet.subsurface((i* 1200, 0), (1200, 675))
    background_frames.append(background_frame)
background_frame_index = 0

terra_spritesheet = pygame.image.load("Assets/background/terra.png").convert_alpha()
terra_frames = []
for i in range(77):
    terra_frame = terra_spritesheet.subsurface((i * 96, 0), (96, 62))
    terra_frames.append(terra_frame)
terra_frame_index = 0

cat_spritesheet = pygame.image.load("Assets/background/cat.png").convert_alpha()
cat_frames = []
for i in range(35):
    cat_frame = cat_spritesheet.subsurface((i* 220, 0), (220, 239))
    cat_frames.append(cat_frame)
cat_frame_index = 0

logo_imagem = pygame.image.load("Assets/background/logo.png")

botao_start_spritesheet = pygame.image.load("Assets/botoes/botao_start.png")
botao_start_frames = []
for i in range(5):
    botao_start_frame = botao_start_spritesheet.subsurface((i * 64, 0), (64, 16))
    botao_start_frames.append(botao_start_frame)
botao_start_frame_index = 0
botao_start = Botao(380, 300, botao_start_frames, botao_start_frame_index, 400, 100, 1)

botao_quit_spritesheet = pygame.image.load("Assets/botoes/botao_quit.png")
botao_quit_frames = []
for i in range(5):
    botao_quit_frame = botao_quit_spritesheet.subsurface((i * 64, 0), (64, 16))
    botao_quit_frames.append(botao_quit_frame)
botao_quit_frame_index = 0
botao_quit = Botao(380, 400, botao_quit_frames, botao_quit_frame_index, 400, 100, 1)

jogador_atirando_spritesheet = pygame.image.load('Assets/jogador/atirando.png')
jogador_atirando_frames = []
for i in range(7):
    jogador_atirando_frame = jogador_atirando_spritesheet.subsurface((i * 64, 0), (64, 64))
    jogador_atirando_frames.append(jogador_atirando_frame)
jogador_atirando_frame_index = 0
jogador = Jogador(600, 400, 300, 300, 5, jogador_atirando_frame_index, jogador_atirando_frames)

def tela_inicial():
    tela.fill((0, 0, 0))

    global background_frame_index
    tela.blit(background_frames[int(background_frame_index)], (0, 0))
    background_frame_index += 0.15
    if background_frame_index > 8:
        background_frame_index = 0

    global terra_frame_index
    terra_frame = terra_frames[int(terra_frame_index)]
    terra_frame_ampliado = pygame.transform.scale(terra_frame, (3200, 1600))
    tela.blit(terra_frame_ampliado, (-1000, 500))
    terra_frame_index += 0.20
    if terra_frame_index > 76:
        terra_frame_index = 0

    logo_imagem_redimensionada = pygame.transform.scale(logo_imagem, (600, 400))
    tela.blit(logo_imagem_redimensionada, (330, -70))

    botao_start.desenhar(tela)
    botao_start.verificar_clique()

    botao_quit.desenhar(tela)
    botao_quit.verificar_clique()
        
def tela_jogando():
    tela.fill((0,0,0))

    global background_frame_index
    tela.blit(background_frames[int(background_frame_index)], (0, 0))
    background_frame_index += 0.15
    if background_frame_index > 8:
        background_frame_index = 0

    global terra_frame_index
    terra_frame = terra_frames[int(terra_frame_index)]
    terra_frame_ampliado = pygame.transform.scale(terra_frame, (3200, 1600))
    tela.blit(terra_frame_ampliado, (-1000, 500))
    terra_frame_index += 0.20
    if terra_frame_index > 76:
        terra_frame_index = 0

    jogador.desenhar(tela)
    jogador.andar()
    jogador.atirar()

def tela_3():
    tela.fill((0,0,0))

    global background_frame_index
    tela.blit(background_frames[int(background_frame_index)], (0, 0))
    background_frame_index += 0.15
    if background_frame_index > 8:
        background_frame_index = 0

    global terra_frame_index
    terra_frame = terra_frames[int(terra_frame_index)]
    terra_frame_ampliado = pygame.transform.scale(terra_frame, (3200, 1600))
    tela.blit(terra_frame_ampliado, (-1000, 500))
    terra_frame_index += 0.20
    if terra_frame_index > 76:
        terra_frame_index = 0

    global cat_frame_index
    tela.blit(cat_frames[int(cat_frame_index)], (490, 218))
    cat_frame_index += 0.20
    if cat_frame_index > 35:
        cat_frame_index = 0

tela_atual = 0

rodando = True
while rodando:
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
    if tela_atual == 0:
        tela_inicial()
        if botao_start.valor == 1:
            tela_atual = 1
        if botao_quit.valor == 1:
            rodando = False
            
    if tela_atual == 1:
        tela_jogando()
    
    if jogador.tela_3 == True:
        tela_atual = 2

    if tela_atual == 2:
        tela_3()
        
    pygame.display.flip()