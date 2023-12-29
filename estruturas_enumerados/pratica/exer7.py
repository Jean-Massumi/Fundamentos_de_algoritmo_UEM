# Análise:
#   Projetar uma estrutura para representar resolucoes(altura e largura em pixels) de tela 
#   e imagens.
#   Projete uma função para cada um dos itens abaixo:
#   a) Determinar quantos mega pixels uma imagem tem ,dada a sua resolução
#   b) Receba duas resoluções(imagem e tela) e verifique se a imagem pode ser exibida completamente
#      na tela sem rotação ou redução da imagem.
#   c) Indique se uma resolução tem aspecto(razão entre largura e altura) de 4:3,
#      16:9 ou outro (projete um tipo enumerado para representar o aspecto). Por exemplo, a
#      resolução 1080 × 1920 tem aspecto 16:9, pois 1080 × 16 = 1920 × 9.

# Definicao:
#   O número de megapixel pode ser caculado multiplicando-se a altura e largura e dividindo-se por
#   1 milhão.
#   A altura e largura serão representados por valores inteiros positivos.

from dataclasses import dataclass
from enum import Enum,auto

@dataclass
class Resolucoes:
    '''
        Estrutura para representar a algura e largura em pixels de uma imagem e tela.  
    '''
    ALTURA : int
    LARGURA : int

class Aspecto(Enum):
    '''
        Aspecto que representa uma resolução.
    '''
    A4x3 = auto()
    A16x9 = auto()
    OUTRO = auto()


def mega_pixels(r:Resolucoes) -> float:
    '''
        Determinar quantos mega pixels uma imagem tem ,dada a sua resolução

    Exemplos:
    >>> mega_pixels(Resolucoes(1080,1920))
    2.0736
    >>> mega_pixels(Resolucoes(5600,4320))
    24.192
    >>> mega_pixels(Resolucoes(720,480))
    0.3456
    '''
    return r.ALTURA * r.LARGURA / 1000000


def duas_resolucoes(imagem:Resolucoes, tela:Resolucoes):
    '''
        Produz True se a imagem pode ser exibida na tela sem a necessidade de rotacao ou reduzao.
        Produz False caso contrario.

    Exemplos:
    >>> duas_resolucoes(Resolucoes(2500,1700), Resolucoes(1820,1580))
    False
    >>> duas_resolucoes(Resolucoes(1000,800), Resolucoes(1000,800))
    True
    >>> duas_resolucoes(Resolucoes(1350,600), Resolucoes(1100,990))
    False
    >>> duas_resolucoes(Resolucoes(540,330), Resolucoes(770,430))
    True
    >>> duas_resolucoes(Resolucoes(1450,2600), Resolucoes(1600,2300))
    False
    '''
    return imagem.ALTURA <= tela.ALTURA and imagem.LARGURA <= tela.LARGURA



def aspecto_resolucao(r:Resolucoes):
    '''
        Determinar o aspecto de uma resolucao r.

        Se a largura * 4 == altura * 3 , devolve o aspecto 4:3 da resolucao.
        Se a largura * 16 == altura * 9 , devolve o aspecto 16:9 da resolucao.
        Senao nao for nenhuma devolve outro aspecto da resolucao.
    
    Exemplos:
    >>> aspecto_resolucao(Resolucoes(2160, 3840 )).name
    'A16x9'
    >>> aspecto_resolucao(Resolucoes(480, 640)).name
    'A4x3'
    >>> aspecto_resolucao(Resolucoes(1100, 1100)).name
    'OUTRO'
    '''

    if r.ALTURA * 4 == r.LARGURA * 3:
        aspecto = Aspecto.A4x3
    elif r.ALTURA * 16 == r.LARGURA * 9:
        aspecto = Aspecto.A16x9
    else:
        aspecto = Aspecto.OUTRO

    return aspecto