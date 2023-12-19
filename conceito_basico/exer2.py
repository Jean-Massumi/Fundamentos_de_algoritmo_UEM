'''
    Analise: 
        Calcular o valor de centimetros para polegagas e vice-versa.
    Definiçao:
        As informaçoes sao a polegadas(1= 2,54 cm) e centimetros(2,54 cm = 1 p).
        Os valores serao representados por numeros positivos.
as 
'''

def main():
    n1:float = float(input('Polegadas: '))
    n2:float = float(input('Centimetros: '))

    resp =polegadas_cen(n1)
    rsp2 =centimetros_pole(n2)

    print(f'Polegadas: {resp:.2f}')
    print(f'Centimetos: {rsp2:.2f}')
    


def polegadas_cen(n1:float) -> float:
    '''
        Especificação:
            A funcao vai receber uma entrada float que irá fazer a conversao para centimetros.
    '''
    centimetros:float = n1 * 2.54

    return centimetros


def centimetros_pole(n1:float) -> float:
    '''
        Especificação:
            A funcao vai receber uma entrada float que ira fazer a conversao para polegadas.
    '''
    polegadas:float = n1/2.54

    return polegadas


main()




