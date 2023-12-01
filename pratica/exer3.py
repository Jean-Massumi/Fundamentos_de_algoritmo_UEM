'''
    Analise:
        Calcular a area de um retangulo atraves da largura e altura.

    Definicao:
        A largura e a altura sera em centimentros com valores positivos.
'''

# def main():
#     largura = int(input('Largura: '))
#     altura = int(input('Altura: '))

#     resp = area_retangulo(largura,altura)
#     print(f'A area de um retangulo de {largura} x {altura} é {resp}')


def area_retangulo(lar:float, alt:float) -> float:
    '''
        A funcao vai receber duas entradas *largura* e *altura* e vai calcular a area de um retangulo.

    Exemplos:
    >>> area_retangulo(3.0, 5.0)
    15.0
    >>> area_retangulo(2.0, 2.5)
    5.0
    '''

    return lar * alt

# main()