# Analise:
#   Verificar se um numero está em uma lista de numeros

def verifica(lista: list, n: int, qt: int) -> bool:
    '''
    Devolve True se o numero estiver na lista, False caso contrario.

    Exemplos:
    >>> verifica([5,2,1,8,3], 3, 5)
    True
    >>> verifica([5,2,1,8,3], 11, 5)
    False
    '''

    if qt == 0:
        return False
    else:
        return n == lista[qt - 1] or verifica(lista, n, qt - 1)





















