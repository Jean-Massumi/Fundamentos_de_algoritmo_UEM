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

        O número de megapixel pode ser caculado multiplicando-se a altura e largura e dividindo-se por
        1 milhão.
    Exemplos:
    >>> mega_pixels(Resolucoes(1080,1920))
    2.0736
    >>> mega_pixels(Resolucoes(5600,4320))
    24.192
    >>> mega_pixels(Resolucoes(720,480))
    0.3456
    '''
    return r.ALTURA * r.LARGURA / 1000000












