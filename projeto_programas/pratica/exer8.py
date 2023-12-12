'''
    Analise:
        Recebemos uma frase que retorne a mesma a frase mas somente com a primeira letra em 
        maiuscula.

    Definicao: 
        A frase recebida devera ser uma string    
'''

def primeira_maiuscula(frase:str) -> str:
    '''
        Analisamos a frase recebida e retornamos somente a primeira letra dela em maiuscula.

        Requer que a *frase* comece com uma letra.
    Exemplos:

    >>> primeira_maiuscula('joao venceu.')
    'Joao venceu.'
    >>> primeira_maiuscula('A Paula é um sucesso.' )
    'A paula é um sucesso.'
    '''

    return frase[:1].upper() + frase[1:].lower()
















