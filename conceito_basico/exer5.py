'''
    Analise:
        Calcular a unidade, dezena e centena de cada numero em uma funcao diferente.
    Definicao:
        Cada funcao deve retornar o calculo de um numero positivo inteiro  unidade, dezena e centena.
'''

def main():
    n =(input('Digite um numero: '))
    n_int:int= int(n)

    x = unidade(n_int)
    y = dezena(n_int)
    z = centena(n_int)
    u = ultimos_digitos(n)

    print(f'A unidade é {x}')
    print(f'A dezena é {y}')
    print(f'A centena é {z}')
    print(f'Resultado: {u}')


def unidade(n1) -> int:
    '''
    Especificação:
        A funcao vai receber uma entrada e deve calcular a unidade de um numero inteiro positivo e retornar 
        qual será a unidade desse numero.
    '''

    # unid = n1[-1]
    unid = n1 % 10

    return unid


def dezena(n1) -> int:
    '''
    Especificação:
        A funcao vai receber uma entrada e deverá calcular a dezena de um numero inteiro positivo e retornar 
        qual será a dezena desse numero.
    '''

    # dez = n1[-2]
    dez = n1 // 10 % 10

    return dez


def centena(n1) -> int:
    '''
    Especificação:
        A funcao vai receber uma entrada e deverá calcular a centena de um numero inteiro positivo e retornar 
        qual será a centena desse numero.
    '''

    # cen = n1[-3]
    cen = n1 // 100 % 10

    return cen


def ultimos_digitos(n1):
    '''
    Especificação:
        A funcao vai receber uma entrada e deverá verificar se os dois ultimos digitos sao 00 e ira retornar 
        com True or False.
    >>> ultimos_digitos('1300')
    'True, os dois ultimos digitos terminam em 00'
    >>> ultimos_digitos('1670')
    'False, os dois ultimos digitos nao terminam em 00'
    >>> ultimos_digitos('1201')
    'False, os dois ultimos digitos nao terminam em 00'
    '''

    if n1[-2:] == '00':
        resp = 'True, os dois ultimos digitos terminam em 00'
    else:
        resp = 'False, os dois ultimos digitos nao terminam em 00'

    return resp


main()