# Análise:
#   Determinar quantos caracteres de uma mensagem ,devem ser exibidos em um determinado momento
#   em um letreiro que pode exibir um determinado numero de caracteres.

# Definição:
#   A mensagem recebida será armazenada em um string.
#   O momento da mensagem sera em um numero inteiro.

from dataclasses import dataclass

@dataclass
class Letreiro:
    TEXTO : str
    EXIBIR_TEXTO : str
    NUMEROS_CARACTERES : int
    MOMENTO : int


def exibir_letreiro(exibir:Letreiro) -> str:
    '''
        Determinar quantos *numeros_caracteres* de uma *texto* ,devem ser *exibidos* em um determinado 
        *momento* em um letreiro que pode exibir um determinado numero de caracteres.
    
    Exemplos:
    >>> exibir_letreiro(Letreiro('Promoção de sorvete, pague 2 leve 3!' , ' ', 20 , 25))
    'e 2 leve 3! Promoção'
    '''

    for i in range(exibir.MOMENTO):
        exibir.EXIBIR_TEXTO = exibir.TEXTO[i:exibir.NUMEROS_CARACTERES] + exibir.TEXTO[:i] 
        if i == i:
            # print(f'MOMENTO {i}')
            print(f'{exibir.EXIBIR_TEXTO}')

        

    return exibir.EXIBIR_TEXTO


exibir_letreiro(Letreiro('Promoção de sorvete, pague 2 leve 3!' , ' ', 20 , 25))



















