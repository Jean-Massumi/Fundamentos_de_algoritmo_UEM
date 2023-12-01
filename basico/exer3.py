'''
    Analise:
        Receber o dia/mes/ano .
    Definicao:
        As informacoes sao dia/mes/ano que sera gerado em str.

'''

def main():
    dia = input('Dia Atual:')
    mes = input('Mes Atual:')
    ano = input('Ano Atual:')

    resp = data_contrario(dia,mes,ano)

    print(f'Ano/Mes/Dia : {resp}')

def data_contrario(dia:int,mes:int, ano:int) ->str:
    '''
        Especificação:
        A funcao vai receber tres tipos de entradas dia,mes e o ano respectivamente e vai gerar em string
        de forma ano/mes/dia.
    '''
    data = (f'{ano}/{mes}/{dia}')

    return data


# def data2(data:str) -> str:
#     print('EXEMPLO: dia/mes/ano - 23/03/1987 ')
#     date:str = (f'{data[-4:]}/{data[3:5]}/{data[:2]} ') 
#     return date

# print(f'Ano/Mes/Dia: {data2("14/01/2004")}')


main()


