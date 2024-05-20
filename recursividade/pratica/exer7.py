# Analise:
#   Colocar todos os valores positivos de uma lista de numeros em uma nova lista.

def lista_positivos(lst: list[int], inicio: int) -> list:
    '''
    Devolve uma nova lista com todos os valores positivos de uma lista de números

    Exemplos
    >>> lista_positivos([-4, -7, -1, 0, 1, 10, 14], 7)
    [1, 10, 14]
    >>> lista_positivos([21, -4, -2, 17, 23, -9], 6)
    [21, 17, 23]
    '''

    if inicio == 0:
        return []
    else:
        nova_lista = lista_positivos(lst, inicio - 1)
        if lst[inicio - 1] > 0:
            nova_lista.append(lst[inicio - 1])
        return nova_lista

print(lista_positivos([21, -4, -2, 17, 23, -9], 6))
