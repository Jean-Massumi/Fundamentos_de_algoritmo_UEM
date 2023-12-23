# Análise:
#   Determinar se as 3 primeiras cartas de um baralho bem embaralhado está em ordem crescente, decrescente ou 
#   não ordenado.

# Definição:
#   As cartas estão enumeradas de 1 a 13.

from dataclasses import dataclass
from enum import Enum,auto

class Ordenada(Enum):
    CRESCENTE = auto()
    DECRESCENTE = auto()
    NÃO_ORDENADA = auto()

@dataclass
class Baralho:
    TRES_PRIMEIRAS_TOPO : list

def sequencia(b:Baralho) -> str:
    '''
        Determinar se as tres primeiras cartas de um batalho bem embaralhado está em ordem crescente,
        decrescente ou nao nao ordenada.

        As cartas estão enumeradas de 1 a 13 e elas não se repetem.

    Exemplos:
    >>> sequencia(Baralho([2,7,12])).name
    'CRESCENTE'
    >>> sequencia(Baralho([13,5,1])).name
    'DECRESCENTE'
    >>> sequencia(Baralho([9,2,8])).name
    'NÃO_ORDENADA'

    '''

    if b.TRES_PRIMEIRAS_TOPO[0] < b.TRES_PRIMEIRAS_TOPO[1] < b.TRES_PRIMEIRAS_TOPO[2]:
        ordem = Ordenada.CRESCENTE
    elif b.TRES_PRIMEIRAS_TOPO[0] > b.TRES_PRIMEIRAS_TOPO[1] > b.TRES_PRIMEIRAS_TOPO[2]:
        ordem = Ordenada.DECRESCENTE
    else:
        ordem = Ordenada.NÃO_ORDENADA

    return ordem    
























