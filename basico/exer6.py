'''
    Analise:
        Verificar se o primeiro nome é *Paula*.
    Definicao:
        O nome da pessoa nao deve ter espacos no inicio e no final e devera conter pelo menos um espaco em branco.
'''

def main():
    x = input('Nome: ')

    rsp = primeiro_nome(x)

    print(f'{rsp}')

def primeiro_nome(nome:str) ->bool:
    '''
        A funcao vai receber uma entradar e ira verificar se o primeiro nome é Paula, caso for , ira retornar 
        True, senao False.
    '''

    verificacao = 'Paula'
    if verificacao == nome[:5]:
        return True
    else:
        return False
    

main()