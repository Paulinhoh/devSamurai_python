#!pip install pygame

import pygame
from pygame.locals import *
import random
import time


WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
POS_INICIAL_X = WINDOWS_WIDTH / 2
POS_INICIAL_Y = WINDOWS_HEIGHT / 2
BLOCK = 10


def colisao(pos1, pos2):
    return pos1 == pos2


def verifica_margens(pos):
    if 0 <= pos[0] < WINDOWS_HEIGHT and 0 <= pos[1] < WINDOWS_HEIGHT:
        return False
    else:
        return True


def gera_posicao_aleatoria(obstaculo_pos):
    x = random.randint(0, WINDOWS_WIDTH)
    y = random.randint(0, WINDOWS_HEIGHT)
    
    if (x,y) in obstaculo_pos:
        return gera_posicao_aleatoria(obstaculo_pos)
    
    return (x // BLOCK * BLOCK), (y // BLOCK * BLOCK)


def game_over():
        fonte = pygame.font.SysFont('arial', 60, True, True)
        game_over = 'GAME OVER'
        text_over = fonte.render(game_over, True, (255,255,255))
        window.blit(text_over, (110, 300)) # type: ignore
        pygame.quit()
        quit()


def main(): 
    pontos = 0
    velocidade = 10

    pygame.font.init()
    fonte = pygame.font.SysFont('arial', 35, True, True)

    pygame.init()
    window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
    pygame.display.set_caption('Jogo da Cobrinha')
    
    cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y), (POS_INICIAL_X + BLOCK, POS_INICIAL_Y), (POS_INICIAL_X + 2*BLOCK, POS_INICIAL_Y)]
    cobra_surface = pygame.Surface((BLOCK,BLOCK))
    cobra_surface.fill((53,59,72))
    direcao = K_LEFT
    
    obstaculo_pos = []
    obstaculo_surface = pygame.Surface((BLOCK,BLOCK))
    obstaculo_surface.fill((0,0,0))
    
    maca_surface = pygame.Surface((BLOCK,BLOCK))
    maca_surface.fill((255,0,0))
    maca_pos = gera_posicao_aleatoria(obstaculo_pos)
    
    while True:
        pygame.time.Clock().tick(velocidade)
        window.fill((68,189,50))
        
        msg = f'Pontos: {pontos}'
        texto = fonte.render(msg,  True, (255,255,255))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()   
            elif event.type == KEYDOWN:
                if event.key in [K_RIGHT, K_LEFT, K_UP, K_DOWN]:
                    if event.key == K_UP and direcao == K_DOWN:
                        continue
                    elif event.key == K_DOWN and direcao == K_UP:
                        continue
                    elif event.key == K_LEFT and direcao == K_RIGHT:
                        continue
                    elif event.key == K_RIGHT and direcao == K_LEFT:
                        continue
                    else:
                        direcao = event.key
        
        window.blit(maca_surface, maca_pos)
        
        if colisao(cobra_pos[0], maca_pos):
            cobra_pos.append((-10,-10))
            maca_pos = gera_posicao_aleatoria(obstaculo_pos)
            obstaculo_pos.append(gera_posicao_aleatoria(obstaculo_pos))
            pontos += 1 
            if pontos % 5 == 0:
                velocidade += 2 
            
        for obstaculo in obstaculo_pos:
            if colisao(cobra_pos[0],pos):  # type: ignore
                game_over()
            window.blit(obstaculo_surface, obstaculo)
        
        for pos in cobra_pos:
            window.blit(cobra_surface, pos)
            
        for item in range(len(cobra_pos)-1,0,-1):
            if colisao(cobra_pos[0], cobra_pos[item]):
                game_over()
            cobra_pos[item] = cobra_pos[item-1]
        
        if verifica_margens(cobra_pos[0]) == True:
            game_over()
            
        if direcao == K_RIGHT:
            cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1] # movimenta para a direita
        elif direcao == K_LEFT:
            cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1] # movimenta para a esquerda
        elif direcao == K_UP:
            cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK # movimenta para a cima
        elif direcao == K_DOWN:
            cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK # movimenta para a baixo
        
        window.blit(texto, (420,30))
        pygame.display.update()


if __name__ == "__main__": 
    main()