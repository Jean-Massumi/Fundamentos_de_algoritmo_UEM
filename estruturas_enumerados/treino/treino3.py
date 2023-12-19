from dataclasses import dataclass

class Seis_numeros:
    a : int
    b : int
    c : int
    d : int
    e : int
    f : int

def sorteado(n:int, sorteados:Seis_numeros) -> bool:
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



def numero_acertos(aposta: Seis_numeros, sorteados: Seis_numeros) -> int:
    '''
    Determina quantos números da *aposta* estão em *sorteados*.
    Exemplos
    >>> numero_acertos(SeisNumeros(1, 2, 3, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    0
    >>> numero_acertos(SeisNumeros(8, 2, 3, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    1
    >>> numero_acertos(SeisNumeros(8, 12, 3, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    2
    >>> numero_acertos(SeisNumeros(8, 12, 20, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    3
    >>> numero_acertos(SeisNumeros(8, 12, 20, 41, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    4
    >>> numero_acertos(SeisNumeros(8, 12, 20, 41, 52, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    5
    >>> numero_acertos(SeisNumeros(8, 12, 20, 41, 52, 57), SeisNumeros(8, 12, 20, 41, 52, 57))
    6
    '''


















