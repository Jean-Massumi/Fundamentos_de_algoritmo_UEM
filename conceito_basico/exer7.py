'''
    Analise:
        Verificar se o ultimo nome da pessoa é *Silva*.
    Definicao:
        A entrada vai ser uma string ,onde nao devera ter espaco no inicio e no final, mas deve conter pelo
        menos um espaco em branco.
'''

def main():
    x = input('Nome: ')

    resp = ultimo_nome(x)

    print(resp)

def ultimo_nome(sobrenome:str) :
    '''
        A funcao vai verificar o ultimo nome da pessoa, caso o ultimo nome da pessoa for *Silva* , ela ira retornar
        True, senao False.    
    '''

    if sobrenome[-5:] == 'Silva':
        verificacao = True
    else:
        verificacao = False

    if verificacao == True:
        res ='O ultimo nome da pessoa é Silva'
    else:
        res ='O ultimo nome da pessoa nao é Silva'

    return res


main()