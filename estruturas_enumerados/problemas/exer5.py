# Análise:
#   Classificar um nome de acordo com uma quantidade x de letras .

# Definição:
#   A classificação deverá ser curto, mediano ou longo.

from enum import Enum, auto

class Nome(Enum):
    CURTO = auto()
    MEDIANO = auto()
    LONGO = auto()

def tamanho_nome(nome:str) -> Nome:
    '''
        Classificar se um *nome* de uma pessoa é curto, mediano ou longo de acordo com o tamanho dela.
    
    Exemplos:
    >>> tamanho_nome('Ana').name
    'CURTO'
    >>> tamanho_nome('Beatriz').name
    'MEDIANO'
    >>> tamanho_nome('Antonieta').name
    'LONGO'
    '''
    if len(nome) <= 4:
        tamanho = Nome.CURTO
    elif len(nome) > 8:
        tamanho = Nome.LONGO
    else:
        tamanho = Nome.MEDIANO

    return tamanho



















