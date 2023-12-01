'''
    Analise: 
        Encontra o maior valor entre dois numeros.
    Definicao:
        Os numeros tem que ser valor inteiros.
'''

def main():
    n1:int = int(input('Primeiro numero: '))
    n2:int = int(input('Segundo numero: '))

    resp = maior(n1,n2)

    print(f'O maior numero entre {n1} e {n2} é {resp}')


def maior(x,y) -> int:
    '''
        A funcao ira receber dois tipos de entradas e devera verificar qual dos dois numeros  é o maior, e ira 
        retorna ele. 
    '''    
    maior1 = 0

    if x > y :
        maior1 = x
    else:
        maior1 = y

    return maior1


main()