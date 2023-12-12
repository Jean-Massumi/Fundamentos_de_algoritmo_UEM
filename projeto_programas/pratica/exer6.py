'''
    Analise:
        Calcular um numero *n* que devolva um novo numero *n* com as dezenas e unidades igual a 0.

    Definição:
        O valor de *n* devera ser um numero natural .
'''

def zerar_dezena_unidade(n:int) -> int:
    '''
        Calcular um numero *n* que devolva um novo numero *n* com as dezenas e unidades igual a 0, onde *n* é um 
        numero natural.

    Exemplos:
    >>> zerar_dezena_unidade(7)
    0
    >>> zerar_dezena_unidade(19)
    0
    >>> zerar_dezena_unidade(341)
    300
    >>> zerar_dezena_unidade(5251)
    5200
    >>> zerar_dezena_unidade(82343)
    82300
    '''
    
    novo_n:int = n - (n % 100)

    return novo_n    
        








