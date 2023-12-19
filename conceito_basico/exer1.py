'''
    Analise:
        Calcular o valor da Hipotenusa atraves dos valores dos catetos.
    Definição:
        Com o valores do catetos , fazemos os calculos para achar a hipotenusa.

        
'''

def main():
    '''
        A funcao serve como entrada e saida de dados.    
    '''
    n1:float = float(input('Cateto 1: '))
    n2:float = float(input('Cateto 2: '))

    resp = calcular_hipotenusa(n1,n2)

    print(f'A Hipotenusa é {resp:.2f}')

def calcular_hipotenusa(co:float,ca:float) -> float:
    '''
        Especificação: 
            A funçao vai receber duas entradas(ca,co) e com isso vai calcular o valor
            da hipotenusa.
    '''
    hip: float =((co)**2 + (ca)**2)**(1/2)

    return hip


main()


