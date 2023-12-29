# Análise:
#   Eliminar os valores incorretos de uma sequência de valores produzidas pelo equipamento.

# Denifição:
#   A lista de sequencia será representado por valores Reais.

def eliminar_negativos(sequencia:list) -> list :
    '''
        Devolve a *sequencia* sem os numeros negativos em uma outra lista

    >>> eliminar_negativos([3, -4, -2, 21, -8, 34, 76, 23, -1])   
    [3, 21, 34, 76, 23]
    >>> eliminar_negativos([-0.7, -101, 5, 41, -16, -0.234, 0.1, 0.45])
    [5, 41, 0.1, 0.45]
    '''
    valores_correto = sequencia[:]
    for n in sequencia:
        if n < 0:
            valores_correto.remove(n)

    return valores_correto

