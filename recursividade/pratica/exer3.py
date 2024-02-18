# Analise:
#   Cria uma lista de numeros a partir de uma lista de string, convertando cada string 
#   para um numero.

# Definicao:
#   Cada string representa numeros validos.

def conversao(lst: list[str], qtd: int) -> list[int]:
    '''
    Devolve uma nova lista de inteiros a partir de uma lista de strings.

    Exemplos:
    >>> conversao(['casa', 'roupa', 'celular'], 3)
    [1, 2, 3]
    >>> conversao([], 0)
    []
    '''

    if qtd != 0:
        lst[qtd - 1] = qtd
        conversao(lst, qtd - 1)

    return lst








