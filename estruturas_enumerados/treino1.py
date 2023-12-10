from enum import Enum, auto

class Cor(Enum):
    AMARELO = auto()
    VERDE = auto()
    VERMELHO = auto()

def proxima_cor(atual:Cor) -> Cor:
    '''
    Exemplos:
    >>> proxima_cor(Cor.VERDE).name
    'AMARELO'
    >>> proxima_cor(Cor.AMARELO).name
    'VERMELHO'
    >>> proxima_cor(Cor.VERMELHO).name
    'VERDE'

    '''

    if atual == Cor.VERDE:
        proxima = Cor.AMARELO

    elif atual == Cor.AMARELO:
        proxima = Cor.VERMELHO

    elif atual == Cor.VERMELHO:
        proxima = Cor.VERDE

    return proxima

c = proxima_cor(Cor.VERDE).name
print(c)

