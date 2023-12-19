'''
    Analise:
        Calcular o imposto de renda de um cidadao, se a renda for menor que 1000 , paga 5% de imposto, entre
        1000 a 5000 paga 5% de imposto sobre os 1000, mais 10% do que passar de 1000 e se recebe mais de 5000
        paga 5% sobre os 1000, 10% sobre 4000 e 20% sobre o que passar de 5000 .

    Definicao:
        A renda e o imposto serao representados por numeros positivos

'''

def imposto(renda:float) ->float:
    '''
    Calcular o imposto de *renda* de um cidadao.

    se renda <= 1000 , imposto 5%.
    se 1000 < renda <= 5000 , imposto de 5% de 1000 + 10% de (renda - 1000)
    se renda > 5000 , imposto de 5% de 1000 + 10% de (renda-4000) + 20% de (renda-5000)
    
    Exemplos:

    >>> imposto(900.0)
    45.0
    >>> imposto(1200.0)
    70.0
    >>> imposto(1800.0)
    130.0
    >>> imposto(6270.0)
    704.0

    ''' 

    if renda <= 1000:
        total_imposto = renda * 5/100
    elif 1000 < renda <= 5000 :
        total_imposto = 50.0 + (renda - 1000.0) * 10/100
    else:
        total_imposto = 50.0 + 400.0 + (renda - 5000.0) * 20/100

    return total_imposto



#qw



















