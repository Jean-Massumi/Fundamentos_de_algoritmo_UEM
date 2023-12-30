# Análise:
#   Determinar 6 numeros para serem sorteados de 1 a 60 na Mega-sena.

# Definição:
#   Os numeros serao representados por valores inteiros positivos.

# from random import randint, sample
# from os import system

# def sorteio(sorteados) -> int:
#     '''
#         Determinar quais serao os 6 numeros sortedos na Mega-sena.
#     '''

#     system('cls')
#     sorteados = sample(range(1,60),6)

#     return sorted(sorteados)


# print(sorteio(''))




# Análise:
#   Determinar 5 numeros para serem sorteados de 1 a 80 na Quina.

# Definição:
#   Os numeros serao representados por valores inteiros positivos.

from random import randint, sample
from os import system

def sorteio(sorteados) -> int:
    '''
        Determinar quais serao os 5 numeros sortedos na Quina.
    '''
    system('cls')
    sorteados = sample(range(1,80),5)

    return sorted(sorteados)


print(sorteio(''))





























