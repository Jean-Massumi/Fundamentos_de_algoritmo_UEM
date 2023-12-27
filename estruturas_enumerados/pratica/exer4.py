# Análise:
#   Projetar uma enumeração para representar as direções norte, sul, leste e oeste!
#   Projete uma função para cada item abaixo:
#   a- Indique a direção oposta de uma direção.
#   b- Indique qual é a direção que está a 90 graus no sentido horário de outra direção.
#   c- Indique qual é a direção que está a 90 graus no sentido anti-horário de outro direção. Use o item b
#      para fazer a implementação(não use seleção nem operações aritmeticas nessa implementação)

from enum import Enum,auto

class Direcoes(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

def direcao_oposta(d:Direcoes) -> Direcoes:
    '''
        Indicar a direção oposta de uma direção.
    
    Exemplos:
    >>> direcao_oposta(Direcoes.NORTE).name
    'SUL'
    >>> direcao_oposta(Direcoes.SUL).name
    'NORTE'
    >>> direcao_oposta(Direcoes.LESTE).name
    'OESTE'
    >>> direcao_oposta(Direcoes.OESTE).name
    'LESTE'
    '''

    if d == Direcoes.NORTE:
        oposta = Direcoes.SUL
    elif d == Direcoes.SUL:
        oposta = Direcoes.NORTE
    elif d == Direcoes.LESTE:
        oposta = Direcoes.OESTE
    else:
        oposta = Direcoes.LESTE

    return oposta


















