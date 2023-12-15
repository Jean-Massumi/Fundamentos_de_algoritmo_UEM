# Analise:
#
# Calcular o valor da correcao anual de um investimento dependendo da aplicacao no inicio de cada ano que pode
# ser 
#   
# valor <= 2000, taxa de 10% ;
# valor <= 5000 , taxa de 12%; 
# valor > 5000, taxa de 13%

# Definição:
#
# o valor e a taxa serão representados por valores positivos.
# o ano sera representados por valores inteiros positivos.

def investimentos(valor:float) -> float:
    '''
    Calcular o *valor* da corracao do investimento dependendo da aplicacao no inicio de cada *ano*.
    
    se o valor <= 2000, taxa de 10% ;
    se o valor <= 5000 , taxa de 12%; 
    se o valor > 5000, taxa de 13%

    '''
   

    if valor <= 2000:
        valor_reajustado = valor + (valor * 10/100)
    elif valor <= 5000:
        valor_reajustado = valor + (valor * 12/100)
    else:
        valor_reajustado = valor + (valor * 13/100)

    return valor_reajustado

def valor_final(valor_inicial:float, anos:int ) -> float:
    '''
    Exemplos: 

    >>> valor_final(1900, 1)
    2090
    >>> valor_final(3000, 1)
    3360
    >>> valor_final(6700, 1)
    7571

    # mais de 1 ano.
    >>> valor_final(1900, 6)
    3683
    >>> valor_final(4200, 3)
    5953
    >>> valor_final(1900, 10)
    5847
    '''
    for i in range(0,anos):
        valor_inicial =  investimentos(valor_inicial)

    return int(valor_inicial)


print(valor_final(1987, 100))

















