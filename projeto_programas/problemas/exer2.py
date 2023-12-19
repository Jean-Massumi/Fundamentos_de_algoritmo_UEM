'''
    Analise:
        Rotacionar uma string em *n* posicoes a direita.

    Definicao:
        Mover os ultimos *n* caracteres para as primeiras *n* posicoes da string

'''

def rotacionar(palavra:str, n:int) -> str:
    '''
        Rotacionar uma string em *n* posicoes a direita, movendo os ultimos *n* caracteres para as 
        primeiras posicoes da string.
    
        *n* tem que ser um numero natural.

    Exemplos:
    >>> rotacionar('juliana', 3)
    'anajuli'
    >>> rotacionar('marcelio', 5)
    'celiomar'
    >>> rotacionar('justiliano', 7)
    'tilianojus'
    '''

    return palavra[-n:] + palavra[:-n]



















