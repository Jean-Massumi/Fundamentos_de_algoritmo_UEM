# Análise:
#   Transforme uma string para que ela tenha uma quantidade n de caracteres.
#
#   Se a string tem mais de n caracteres, os caracteres excedentes do final devem ser removidos.
#   Se a string tem menos caracteres que n, deve adicionar espaços em branco no final.  

# Definição:
#   O numero *n* será representado por valores inteiros positivos.

def qtd_caracteres(frase:str, n:int) -> str:
    '''
        Transformar uma *frase* string para que ela tenha a mesma quantidade de *n* caracteres.

        Se len(frase) > n , remove os caracteres excedentes do final da frase.
        Se len(frase) < n , adiciona espaços no final da frase .
    
    Exemplos:
    >>> qtd_caracteres('paralelepípedo', 4)
    'para'
    >>> qtd_caracteres('lápis', 5)
    'lápis'
    >>> qtd_caracteres('machado', 10)
    'machado   '
    '''

    if len(frase) > n:
        frase = frase[:n]
    elif len(frase) < n:
        frase = frase + (n - len(frase)) * ' '
    
    return frase
















