import pygame
from botao import Botao
from jogador import Jogador
from tiro import Tiro, Especial
from inimigo import Inimigo
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 36)

LARGURA_TELA = 1200
ALTURA_TELA = 675
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
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
botao_quit = Botao(380, 400, botao_quit_frames, botao_quit_frame_index, 400, 100, 2)

botao_restart = Botao(380, 300, botao_start_frames, 0, 400, 100, 2)
botao_quit_game_over = Botao(380, 400, botao_quit_frames, 0, 400, 100, 3)

jogador_atirando_spritesheet = pygame.image.load('Assets/jogador/atirando.png')
jogador_atirando_frames = []
for i in range(7):
    jogador_atirando_frame = jogador_atirando_spritesheet.subsurface((i * 64, 0), (64, 64))
    jogador_atirando_frames.append(jogador_atirando_frame)
jogador_atirando_frame_index = 0

try:
    paralisia_spritesheet = pygame.image.load('Assets/jogador/paralisia.png')
    paralisia_frames = []
    for i in range(10):
        paralisia_frame = paralisia_spritesheet.subsurface((i * 64, 0), (64, 64))
        paralisia_frames.append(paralisia_frame)
except:
    paralisia_frames = []

try:
    especial_spritesheet = pygame.image.load('Assets/jogador/especial.png')
    especial_frames = []
    for i in range(4):
        especial_frame = especial_spritesheet.subsurface((i * 18, 0), (18, 38))
        especial_frames.append(especial_frame)
except:
    especial_frames = []

jogador = Jogador(600, 400, 300, 300, 5, jogador_atirando_frame_index, jogador_atirando_frames, paralisia_frames, especial_frames)

inimigo_morrendo_spritesheet = pygame.image.load('Assets/jogador/inimigo.png')
inimigo_morrendo_frames = []
for i in range(13):
    inimigo_morrendo_frame = inimigo_morrendo_spritesheet.subsurface((i * 128, 0), (128, 128))
    inimigo_morrendo_frames.append(inimigo_morrendo_frame)
inimigo_morrendo_frame_index = 0

inimigos = []
tempo_ultimo_inimigo = 0
tempo_entre_inimigos = 2000

tiro_spritesheet = pygame.image.load('Assets/jogador/tiro.png')
tiro_frames = []
for i in range(8):
    tiro_frame = tiro_spritesheet.subsurface((i * 8, 0), (8, 8))
    tiro_frames.append(tiro_frame)
tiro_frame_index = 0
tiros = []
tempo_ultimo_tiro = 0
tempo_entre_tiros = 250

especiais = []

def desenhar_fundo(tela, incluir_gato=False):
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

    if incluir_gato:
        global cat_frame_index
        tela.blit(cat_frames[int(cat_frame_index)], (490, 218))
        cat_frame_index += 0.20
        if cat_frame_index > 35:
            cat_frame_index = 0

def tela_inicial():
    tela.fill((0, 0, 0))

    desenhar_fundo(tela)

    logo_imagem_redimensionada = pygame.transform.scale(logo_imagem, (600, 400))
    tela.blit(logo_imagem_redimensionada, (330, -70))

    botao_start.desenhar(tela)
    botao_start.verificar_clique()

    botao_quit.desenhar(tela)
    botao_quit.verificar_clique()
        
def tela_jogando():
    tela.fill((0,0,0))

    desenhar_fundo(tela)

    jogador.desenhar(tela)
    jogador.andar()
    jogador.atirar()

    if jogador.especial_pronto and pygame.key.get_pressed()[pygame.K_e]:
        novo_especial = Especial(jogador.x + 150, jogador.y + 150, 100, 100, 20, 0, especial_frames)
        especiais.append(novo_especial)
        jogador.especial_pronto = False
        jogador.inimigos_derrotados = 0
    global tempo_ultimo_tiro
    agora = pygame.time.get_ticks()
    if jogador.atirando:
        if agora - tempo_ultimo_tiro >= tempo_entre_tiros:
            novo_tiro = Tiro(jogador.x + 145, jogador.y + 100, 16, 16, 10, 0, tiro_frames)
            tiros.append(novo_tiro)
            tempo_ultimo_tiro = agora
    for t in tiros[:]:
        t.desenhar(tela)
        if t.y + t.altura < 0:
            tiros.remove(t)

    for e in especiais[:]:
        e.desenhar(tela)
        if e.y + e.altura < 0:
            especiais.remove(e)

    global tempo_ultimo_inimigo
    agora = pygame.time.get_ticks()
    if agora - tempo_ultimo_inimigo >= tempo_entre_inimigos:
        x_inimigo = random.randint(0, LARGURA_TELA - 300)
        novo_inimigo = Inimigo(x_inimigo, -300, 300, 300, 3, 0, inimigo_morrendo_frames)
        inimigos.append(novo_inimigo)
        tempo_ultimo_inimigo = agora

    for i in inimigos[:]:
        i.mover(jogador)
        i.desenhar(tela)
        if not i.vivo and i.animacao_morte_concluida:
            inimigos.remove(i)

    for i in inimigos[:]:
        if i.collision_rect.colliderect(jogador.collision_rect):
            jogador.paralisado = True
            jogador.tempo_paralisia = pygame.time.get_ticks() + 2000
            i.vivo = False
            break

    for t in tiros[:]:
        for i in inimigos[:]:
            if t.rect.colliderect(i.rect) and i.vivo:
                tiros.remove(t)
                i.vivo = False
                jogador.pontuacao += 10
                jogador.inimigos_derrotados += 1
                if jogador.inimigos_derrotados >= 10:
                    jogador.especial_pronto = True
                break

    for e in especiais[:]:
        for i in inimigos[:]:
            if e.rect.colliderect(i.rect) and i.vivo:
                i.vivo = False
                jogador.pontuacao += 20

    vida_text = font.render(f"Vida: {jogador.vida}", True, (255, 255, 255))
    tela.blit(vida_text, (10, 10))
    pontuacao_text = font.render(f"Pontuação: {jogador.pontuacao}", True, (255, 255, 255))
    tela.blit(pontuacao_text, (10, 50))
    if jogador.especial_pronto:
        especial_text = font.render("Especial Pronto! Pressione E", True, (255, 0, 0))
        tela.blit(especial_text, (10, 90))

def tela_3():
    tela.fill((0,0,0))

    desenhar_fundo(tela, incluir_gato=True)

def tela_game_over():
    tela.fill((0,0,0))

    desenhar_fundo(tela)

    game_over_text = font.render("Game Over", True, (255, 255, 255))
    tela.blit(game_over_text, (500, 200))
    score_text = font.render(f"Pontuação Final: {jogador.pontuacao}", True, (255, 255, 255))
    tela.blit(score_text, (450, 250))

    botao_restart.desenhar(tela)
    botao_restart.verificar_clique()

    botao_quit_game_over.desenhar(tela)
    botao_quit_game_over.verificar_clique()

tela_atual = 0

rodando = True
while rodando:
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if tela_atual == 0:
                if botao_start.rect.collidepoint(mouse_pos):
                    tela_atual = 1
                    botao_start.valor = 0
                if botao_quit.rect.collidepoint(mouse_pos):
                    rodando = False
            if tela_atual == 3:
                if botao_restart.rect.collidepoint(mouse_pos):
                    jogador.x = 600
                    jogador.y = 400
                    jogador.vida = 3
                    jogador.pontuacao = 0
                    inimigos.clear()
                    tiros.clear()
                    tela_atual = 1
                    botao_restart.valor = 0
                if botao_quit_game_over.rect.collidepoint(mouse_pos):
                    rodando = False
        
    if tela_atual == 0:
        tela_inicial()
            
    if tela_atual == 1:
        tela_jogando()
    
    if jogador.tela_3:
        tela_atual = 2
    if jogador.vida <= 0:
        tela_atual = 3

    if tela_atual == 2:
        tela_3()
    
    if tela_atual == 3:
        tela_game_over()
        
    pygame.display.flip()