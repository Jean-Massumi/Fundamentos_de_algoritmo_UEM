'''
    Analise:
        Calcular o aumento de um valor *a* por uma porcentagem *b*    
    
    Definição:
        Os valores de *a* e *b* deveram ser positivos
'''

def aumenta(valor:float, porc:float) -> float:
    '''
        Calcula o aumento do valor *a* pela porcentagem *b* . Os valores de *a* e *b* devem ser positivos.
    Exemplos:
    >>> aumenta(100.0, 3.0)
    103.0
    >>> aumenta(20.0, 50.0)
    30.0
    >>> aumenta(10.0, 80.0)
    18.0
    '''

    aumen:float = valor + (valor * porc/100)

    return aumen

