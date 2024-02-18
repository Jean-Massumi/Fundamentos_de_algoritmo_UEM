# Analise:
#   Concatenar todas as strings de uma lista ,usando recursividade.

def concatene(lista: list[str], qtd: int) -> str:
    '''
    Devolve a concatenaçao de todas as string de uma lista.

    Exemplos:
    >>> concatene(['casa', 'loja', 'mouse', 'pessoa'], 0)
    'casa loja mouse pessoa '
    >>> concatene([], 0)
    ''
    '''

    if qtd == len(lista):
        return ''
    else:
        return str(lista[qtd]) + ' ' + str(concatene(lista, qtd + 1))
























