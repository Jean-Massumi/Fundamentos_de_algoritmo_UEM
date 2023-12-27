# Análise:
#   Determinar 15 numeros para serem sorteados de 1 a 25 na lotofacil.

# Definição:
#   Os numeros serao representados por valores inteiros positivos.

from random import randint, sample
from os import system

def sorteio(sorteados) -> int:
    '''
        Determinar quais serao os 15 numeros sortedos na lotofácil.
    '''
    system('cls')
    sorteados = sample(range(1,25),15)

    return sorted(sorteados)


print(sorteio(''))
















