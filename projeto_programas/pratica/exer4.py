'''
    Analise:
        Calcular o produto de n, n+1  e n-1.
    Definição:
        O valor de n devera ser um numero inteiro.
'''

def produto_anterior_posterior(n:int) -> int:
    '''
        Calculamos o anterior e o posterior de *n* e depois calculamos o produto de n, n-1 e n+1 onde n é um 
        valor inteiro.    

    Exemplos:
    >>> produto_anterior_posterior(3)
    24
    >>> produto_anterior_posterior(1)
    0
    >>> produto_anterior_posterior(-2)
    -6
    '''

    anterior:int = n-1
    posterior:int = n+1

    produto = anterior * n * posterior

    return produto








