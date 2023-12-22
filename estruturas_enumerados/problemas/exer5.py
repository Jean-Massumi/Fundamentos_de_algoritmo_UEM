# Análise:
#   Classificar um nome de acordo com uma quantidade x de letras .

# Definição:
#   A classificação deverá ser curto, mediano ou longo.


def tamanho_nome(nome:str) -> str:
    '''
        Classificar se um *nome* de uma pessoa é curto, mediano ou longo de acordo com o tamanho dela.
    
    Exemplos:
    >>> tamanho_nome('Ana')
    'CURTO'
    >>> tamanho_nome('Beatriz')
    'MEDIANO'
    >>> tamanho_nome('Antonieta')
    'LONGO'
    '''
    if len(nome) <= 4:
        tamanho = 'CURTO'
    elif len(nome) > 8:
        tamanho = 'LONGO'
    else:
        tamanho = 'MEDIANO'

    return tamanho



















