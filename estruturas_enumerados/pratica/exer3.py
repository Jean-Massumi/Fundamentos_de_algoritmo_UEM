# Análise:
#   Encontre qual valor entre 0 e 100 está mais proximo de um dado numero.

# Definição:
#   O numero será representado por um valor inteiro.

def mais_proximo(n:int):
    '''
        Encontrar qual valor entre 0 e 100 está mais proximo de um dado numero.

    >>> mais_proximo(56)
    'Os números mais proximo de 56 sao 55 e 57.'
    >>> mais_proximo(22)
    'Os números mais proximo de 22 sao 21 e 23.'
    >>> mais_proximo(100)
    'O número mais proximo de 100 é 99.'
    >>> mais_proximo(0)
    'O número mais proximo de 0 é 1.'
    >>> mais_proximo(567)
    'O número mais proximo de 567 é 100.'
    >>> mais_proximo(-24)
    'O número mais proximo de -24 é 0.'
    '''

    if n <= 0:
        numero_proximo = f'O número mais proximo de {n} é 0.'
        if n == 0:
            numero_proximo = f'O número mais proximo de {n} é 1.'
    elif n >= 100:
        numero_proximo = f'O número mais proximo de {n} é 100.'
        if n == 100:
            numero_proximo = f'O número mais proximo de {n} é 99.'
    else:
        numero_proximo = f'Os números mais proximo de {n} sao {n-1} e {n+1}.'
    
    return numero_proximo
























