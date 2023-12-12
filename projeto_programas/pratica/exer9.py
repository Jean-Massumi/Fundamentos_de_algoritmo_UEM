'''
    Analise:
        Receberemos dois argumentos sendo uma frase e um numero, onde iremos retornar uma nova frase
        trocando os *n* primeiras letras da frase por *x*.

    Definição:
        A frase recebida devera ser uma string e o valor devera ser um  numero natural.

'''

def censura(frase:str, n:int)->str:
    '''
        Receberemos dois argumentos sendo uma string *frase* e um *numero* natural, onde iremos retornar 
        uma nova frase trocando os *n* primeiras letras da frase por *x*.

    Exemplos:
    >>> censura('droga de lanche!', 5)
    'xxxxx de lanche!'
    >>> censura('ferrou geral!', 6)
    'xxxxxx geral!'
    '''

    return n * 'x' + frase[n:]

















