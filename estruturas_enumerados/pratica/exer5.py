# Análise:
#   Representar o estado de um elevador que pode estar parado , subindo ou descendo.
#   1- Estando o elevador parado, determine a partir do andar atual e do andar solicitada,qual será a 
#      condição do elevador ao atender a solicitação.
#   2- O elevador só pode se movimentar se tiver parado, verifique se um elevador pode passar de um estado
#      para outro.

# Definição:
#   Os numeros dos andares serão representados por valores inteiros positivos.

from enum import Enum,auto

class Estado(Enum):
    '''
        OS tipos de estado que um elevador pode está.    
    '''
    PARADO = auto()
    SUBINDO = auto()
    DESCENDO = auto()


# def estado_elevador(Atual: int , solicitado:int) ->Estado:
#     '''
#         Determinar a partir do andar atual e do andar solicitado, qual será o estado do elevador 
#         ao atender a solicitacao.
    
#     >>> estado_elevador(1, 7).name
#     'SUBINDO'
#     >>> estado_elevador(9, 5).name
#     'DESCENDO'
#     '''

#     if solicitado > Atual:
#         condicao = Estado.SUBINDO
#     else:
#         condicao = Estado.DESCENDO

#     return condicao




# Tabela das 9 posibilidades de entrada do elevador, e as saídas de cada possibilidades.
#
#           Estado Atual    |   Estado Solicitado   |        Saídas   
#               PARADO      |       SUBINDO         |         True          *
#               PARADO      |       DESCENDO        |         True          *
#               PARADO      |       PARADO          |         False              
#               SUBINDO     |       SUBINDO         |         False              
#               SUBINDO     |       DESCENDO        |         False
#               SUBINDO     |       PARADO          |         True          *
#               DESCENDO    |       SUBINDO         |         False
#               DESCENDO    |       DESCENDO        |         False              
#               DESCENDO    |       PARADO          |         True          *
#

def estado_para_outro(estado_atual:str , estado_novo:Estado) :
    '''
        Verificar se o elevador pode passar de um estado para outro.

        Lembrando que o elevador só comeca a se movimentar se tiver parado.
    
    Exemplos:
    >>> estado_para_outro('PARADO', Estado.SUBINDO)
    'FEITO! Passagem de um estado para outro'
    >>> estado_para_outro('PARADO', Estado.DESCENDO)
    'FEITO! Passagem de um estado para outro'
    >>> estado_para_outro('PARADO', Estado.PARADO)
    'ERRO! Problema de passagem de um estado para outro'
    >>> estado_para_outro('SUBINDO', Estado.SUBINDO)
    'ERRO! Problema de passagem de um estado para outro'
    >>> estado_para_outro('SUBINDO', Estado.DESCENDO)
    'ERRO! Problema de passagem de um estado para outro'
    >>> estado_para_outro('SUBINDO', Estado.PARADO)
    'FEITO! Passagem de um estado para outro'
    >>> estado_para_outro('DESCENDO', Estado.SUBINDO)
    'ERRO! Problema de passagem de um estado para outro'
    >>> estado_para_outro('DESCENDO', Estado.DESCENDO)
    'ERRO! Problema de passagem de um estado para outro'
    >>> estado_para_outro('DESCENDO', Estado.PARADO)
    'FEITO! Passagem de um estado para outro'
    '''

    if estado_atual == estado_novo.name :
        verifica = 'ERRO! Problema de passagem de um estado para outro'
    elif (estado_atual == Estado.PARADO.name):
        if (estado_novo == Estado.DESCENDO) or (estado_novo == Estado.SUBINDO):
            verifica = 'FEITO! Passagem de um estado para outro'
    elif (estado_atual == Estado.SUBINDO.name) or (estado_atual == Estado.DESCENDO.name):
        if estado_novo == Estado.PARADO:
            verifica = 'FEITO! Passagem de um estado para outro'
        else:
            verifica = 'ERRO! Problema de passagem de um estado para outro'

    return verifica