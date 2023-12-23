# Análise:
#   Determinar 6 numeros para serem sorteados de 1 a 60 na Mega-sena.

# Definição:
#   Os numeros serao representados por valores inteiros positivos.

from random import randint, sample

def sorteio(sorteados) -> int:
    '''
        Determinar quais serao os 6 numeros sortedos na Mega-sena.
    '''

    sorteados = sample(range(1,60),6)

    return sorted(sorteados)


print(sorteio(''))

































