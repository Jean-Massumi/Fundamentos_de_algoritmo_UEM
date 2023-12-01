'''
    Analise: 
        Descobrir se o nome da pessoa é mediano.
    Definicao:
        Recebemos o nome da pessoa e retornamos o tipo de tamanho dela, curto,mediano ou longo.
'''

def main():
    x = input('Informe seu primeiro nome: ')

    resp = tamanho(x)
    print(f'O nome {x} tem tamanho {resp}')

def tamanho(nome:str) -> str:
    '''
        Especificação:
            A funcao ira receber uma entra(nome) e vai ler o tamanho dele e retornar o tipo de tamanho do nome,
            curto, mediano ou longo.

    >>> tamanho('Ana')
    'CURTO'
    >>> tamanho('Pedro')
    'MEDIANO'
    >>> tamanho('Antonieta')
    'LONGO'
    '''

    if len(nome) <= 3:
        tipo = 'CURTO'
    elif len(nome) > 8:
        tipo = 'LONGO'
    else:
        tipo = 'MEDIANO'

    return tipo

main()

