# Analise:
#   Encontrar o maior valor dentro de uma lista.

# Definicao:
#   A lista nao pode estar vazia

def maior(lst: list[int], qtd: int) -> int:
    '''
    Devolve o maior valor de uma lista nao vazia.

    Exemplos:
    >>> maior([2, 5, 9, 1], 4)
    9
    >>> maior([3], 1)
    3
    >>> maior([1, 2, 11], 3)
    11
    >>> maior([22, 3, 19], 3)
    22
    '''

    if qtd == 1:
        return lst[0]
    else:
        max = maior(lst, qtd - 1)
        if lst[qtd - 1] >= max:
            return lst[qtd - 1]
        elif lst[qtd - 1] < max:
            return max
