# Análise:
#   Representar o estado de um elevador que pode estar parado , subindo ou descendo.
#   1- Estando o elevador parado, determine a partir do andar atual e do andar solicitada,qual será a 
#      condição do elevador ao atender a solicitação.
#   2- O elevador só pode se movimentar se tiver parado, verifique se um elevador pode passar de um estado
#      para outro.

# Definição:
#   Os numeros dos andares serão representados por valores inteiros positivos.

from dataclasses import dataclass
from enum import Enum,auto

class Estado(Enum):
    '''
        OS tipos de estado que um elevador pode está.    
    '''
    PARADO = auto()
    SUBINDO = auto()
    DESCENDO = auto()

@dataclass
class Elevador:
    '''
        Informações do elevador.    
    '''
    ESTADO : Estado
    ANDAR_ATUAL : int
    ANDAR_SOLICITADO : int

def estado_elevador(e:Elevador) ->Estado:
    '''
        Determinar a partir do andar atual e do andar solicitado, qual será o estado do elevador 
        ao atender a solicitacao.
    
    >>> estado_elevador(Elevador(Estado.PARADO, 1, 7)).name
    'SUBINDO'
    >>> estado_elevador(Elevador(Estado.PARADO, 9, 5)).name
    'DESCENDO'
    '''

    if e.ANDAR_SOLICITADO > e.ANDAR_ATUAL:
        condicao = Estado.SUBINDO
    else:
        condicao = Estado.DESCENDO

    return condicao

















