# Analise:
#   Verificar se todos os elementos de uma lista sao binarios

# Definicao:
#   Binario: 0 ou 1

def verificar(lst: list[int], qtd: int) -> bool:
    '''
    Devolve True se todos os elementos da lista for binario, False caso contrario.

    Exemplos:
    >>> verificar([1, 1, 0, 1, 0], 5)
    True
    >>> verificar([3, 5, 6, 1, 0], 5)
    False
    '''

    if qtd == 0:
        return True
    else:
        p = 0 == lst[qtd - 1] or 1 == lst[qtd - 1]
        return p and verificar(lst, qtd - 1)



