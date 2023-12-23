# Análise:
#   Determinar 15 numeros para serem sorteados na lotofacil.

# Definição:
#   Os numeros serao representados por valores inteiros positivos.

from random import randint, sample


def sorteio(sorteados) -> int:
    '''
        Determinar quais serao os 15 numeros sortedos na lotofácil.
    '''

    sorteados = sample(range(1,25),15)

    return sorted(sorteados)


print(sorteio(''))
















