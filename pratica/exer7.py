'''
    Analise:
        Fazemos que uma frase adicione *n* vezes *!* na frase.

    Definição:
        O valor de *n* sera um numero natural.
'''

def exclamacao(frase:str, n:int) -> str:
    '''
        Calculamos *n* vezes *!* e adicionamos a quantidade de *!* na frase.

    Exemplos:
    >>> exclamacao ('Nossa', 3)
    'Nossa!!!'
    >>> exclamacao('Que Legal', 1)
    'Que Legal!'
    >>> exclamacao('Nada', 0)
    'Nada'
    '''

    nova_frase = frase + '!' * n

    return nova_frase





















