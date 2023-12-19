from enum import Enum, auto


class Combustivel(Enum):
    ALCOOL = auto()
    GASOLINA = auto()
 

def indica_combustivel(preco_alcool:float, preco_gasolina:float) -> Combustivel:
    '''
    Exemplos:
    >>> indica_combustivel(4.00, 6.00).name
    'ALCOOL'
    >>> indica_combustivel(3.50, 5.00).name
    'ALCOOL'
    >>> indica_combustivel(4.00, 5.00).name
    'GASOLINA'

    '''

    if preco_alcool <= 0.7 * preco_gasolina:
        combustivel = Combustivel.ALCOOL
    else:
        combustivel = Combustivel.GASOLINA

    return combustivel















