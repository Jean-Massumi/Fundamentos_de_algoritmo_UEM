'''
    Analise:
        Verifique se um texto contem espacos extras.

    Definicao:
        Os espacos extras nao podem conter no inicio e no fim no texto, caso contenha ou nao, devolva 
        uma mensagem avisando se o texto esta de acordo com a regra *sem espaçoes extras*.

'''

def sem_espaco_extras(texto:str):
    '''
        Verificar um *texto* se ha espacos extras no inicio e fim, e devolva uma mensagem avisando
        se está de acordo com a regra! 
    Exemplos:
    >>> sem_espaco_extras(' bom dia, bora trabalhar? ')
    'O texto nao segue de acordo com a regra, pois ha espacos extras no texto.'

    >>> sem_espaco_extras('exatas é melhor que humanas')
    'O texto está de acordo com a regra, nao ha espaco extras no texto.'
    '''

    if texto[0] == ' ' or texto[-1] == ' ':
        return 'O texto nao segue de acordo com a regra, pois ha espacos extras no texto.'

    else:
        return 'O texto está de acordo com a regra, nao ha espaco extras no texto.'
 









