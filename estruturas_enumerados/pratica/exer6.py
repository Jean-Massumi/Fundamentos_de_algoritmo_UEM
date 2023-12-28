# Análise:
#   Projetar uma estrutura para representar uma data com dia , mês e ano.
#   Projete uma função para cada um dos itens abaixo:
#   a)Verificar se uma data é o ultimo dia do ano.
#   b)Receber duas datas e verificar se a primeira vem antes que a segunda.
#   c)Verifique se uma data é valida.Considere que em anos bissextos fevereiro tem 29 dias e que
#     um ano é bissexto se é múltiplo de 400 ou é múltiplo de 4 mas não é múltiplo de 100

# Definição:
#   As datas, dia, mês e ano serão representados por valores inteiros positivos

from dataclasses import dataclass

@dataclass
class Data:
    '''
        Referencia do dia , mes e ano de uma data.
    '''
    DIA : int
    MÊS : int
    ANO : int

def ultimo_dia_ano(d:Data) -> bool:
    '''
        Verificar uma data para saber se é o ultimo dia do ano. Se for devolve *True* senão *False*
    
    Exemplos:
    >>> ultimo_dia_ano(Data(31,12,2023))
    True
    >>> ultimo_dia_ano(Data(31,10,2022))
    False
    '''
    verificar = False
    if (d.DIA == 31) and (d.MÊS == 12) :
        verificar = True

    return verificar


def duas_datas(d1:Data, d2:Data) -> bool:
    '''
        Verificar se a primeira data vem antes da segunda. Se sim devolve *True* senão *False*.

        Em caso de as datas forem iguais, devolve *False*.
    
    >>> duas_datas(Data(14,7,1987), Data(15,9,2000))
    True
    >>> duas_datas(Data(30,8,2005), Data(23,12,2005))
    True
    >>> duas_datas(Data(13,3,2009), Data(15,3,2009))
    True
    >>> duas_datas(Data(23,11,2015), Data(9,1,2003))
    False
    >>> duas_datas(Data(19,12,2030), Data(19,12,2030))
    False
    >>> duas_datas(Data(29,12,2023), Data(14,12,2023))
    False
    >>> duas_datas(Data(1,5,2030), Data(19,4,2030))
    False

    '''

    verificar = False

    if (d1.ANO == d2.ANO and d1.MÊS == d2.MÊS and d1.DIA < d2.DIA) or \
                (d1.ANO == d2.ANO and d1.MÊS < d2.MÊS) or \
                        (d1.ANO < d2.ANO) :
        verificar = True
   
    return verificar


