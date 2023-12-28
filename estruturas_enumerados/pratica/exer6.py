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
        Verificar uma data para saber se é o ultimo dia do ano.
    
    Exemplos:
    >>> ultimo_dia_ano(Data(31,12,23))
    True
    >>> ultimo_dia_ano(Data(31,10,22))
    False
    '''
    verificar = False
    if (d.DIA == 31) and (d.MÊS == 12) :
        verificar = True

    return verificar
















