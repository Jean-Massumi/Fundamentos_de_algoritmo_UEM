from dataclasses import dataclass

class seis_numeros:
    a : int
    b : int
    c : int
    d : int
    e : int
    f : int

def sorteado(n:int, sorteados:seis_numeros) -> bool:
    '''
    Produz True se *n* é um dos números
    em *sorteados*. False caso contrário.
    
    Exemplos:  
    >>> sorteados = SeisNumeros(1, 7, 10, 40, 41, 60)
    >>> sorteado(1, sorteados)
    True
    >>> sorteado(7, sorteados)
    True
    >>> sorteado(10, sorteados)
    True)
    >>> sorteado(40, sorteados)
    True
    >>> sorteado(41, sorteados)
    True
    >>> sorteado(60, sorteados)
    True
    >>> sorteado(2, sorteados)
    False
    '''


    return False


















