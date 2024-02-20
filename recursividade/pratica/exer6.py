# Analise:
#   Encontrar o tamanho maximo  entre todas as string de uma lista de strings.

def maior_str(lst: list[str], qtd: int):
    '''
    Devolve o tamanho maximo entre todas as strings de uma lista de string 
    
    Exemplos:
    >>> maior_str(['novo', 'cachorro', 'lapis', 'celular'], 4)
    8
    >>> maior_str(['teia', 'lapis', 'celular'], 3)
    7
    >>> maior_str(['chave', 'uva', 'relogio'], 3)
    7
    >>> maior_str(['planta'], 1)
    6
    '''

    if qtd == 1:
        return len(lst[0])
    else:
        max = maior_str(lst, qtd - 1)
        if len(lst[qtd - 1]) >= max:
            return len(lst[qtd - 1])
        elif len(lst[qtd - 1]) < max:
            return max


















