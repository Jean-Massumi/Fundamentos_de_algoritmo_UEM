# Análise:
#   Determinar a nova posição do personagem dada a posição atual e uma sequência de deslocamentos.

# Definição:
#   A posição do personagem requer três componentes (x, y, z), por isso será representada por uma estrutura.
#
#   O deslocamento é um de 6 valores, então será representada com uma enumeração

from dataclasses import dataclass
from enum import Enum,auto

@dataclass
class Posicao:
    '''
        Indica a posicao do personagem no mapa    
    '''
    X : int
    Y : int
    Z : int

class Deslocamento(Enum):
    '''
        Indica o deslocamento de um personagem no mapa.

        Norte(+) , Sul(-) , eixo x
        Leste(+) , Oeste(-), eixo y
        Para_cima(+) , Para_baixo(-) , eixo z
    '''
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()
    PARA_CIMA = auto()
    PARA_BAIXO = auto()

def nova_posicao(p:Posicao , d:list[Deslocamento]) -> Posicao:
    '''
        Calcular o novo posicao do personagem , considerando que ele partiu de *p* até *d*.

    Exemplos:
    >>> d = Deslocamento
    >>> nova_posicao(Posicao(9, 1, 0), [d.NORTE, d.PARA_CIMA, d.PARA_CIMA, d.OESTE])
    Posicao(X=10, Y=0, Z=2)
    >>> nova_posicao(Posicao(5, 2, 7), [d.SUL, d.PARA_BAIXO, d.PARA_BAIXO, d.LESTE])
    Posicao(X=4, Y=3, Z=5)
    >>> nova_posicao(Posicao(0, 0, 0), [d.SUL, d.PARA_BAIXO, d.SUL, d.OESTE])
    Posicao(X=-2, Y=-1, Z=-1)
    '''

    for i in d:
        if i == Deslocamento.NORTE:
            p.X += 1
        elif i == Deslocamento.SUL:
            p.X -= 1
        elif i == Deslocamento.LESTE:
            p.Y += 1
        elif i == Deslocamento.OESTE:
            p.Y -= 1
        elif i == Deslocamento.PARA_CIMA:
            p.Z += 1
        else:
            p.Z -= 1

    return Posicao(p.X, p.Y, p.Z)
        












