# Análise:
#   Determine o sinal de um numero, produzindo -1 para valores negaticos , 1 para valores positivos e 0 
#   para 0.

# Definição:
#   O numero será representado por valores Reais.

def sinal(n:float) -> int:
    '''
        Determinar o sinal de um numero, produzindo -1 para valores negativos, 1 para valores positivos e
        0 para 0.
    
    Exemplos:
    >>> sinal(0)
    0
    >>> sinal(-32)
    -1
    >>> sinal(52)
    1
    >>> sinal(-4.21)
    -1
    >>> sinal(9.32)
    1
    '''
    if n < 0:
        s = -1
    elif n > 0:
        s = 1
    else:
        s = 0

    return s









