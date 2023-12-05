'''
    Analise:
        Calcular o tempo que o pintor ira demorar para pintar uma serie de paralelepipedos.

    Definicao:
        O *comprimento* ,*largura* e *altura* será em cm.

'''

def tempo_pintura(larg:float, alt:float, comp:float) :
    '''
        Calcular a area total de um paralelepipedo e logo em seguida dividir por 64cm e multiplicamos
        por 30 segundos.
        Apos saber o tempo de demorar, calculamos a hora, minutos e segundos caso existam.
    Exemplos:
    >>> tempo_pintura(35.56, 93.53, 56)
    9894

    '''

    area_total:int = int(2*(comp*larg + larg*alt + comp*alt))
    tempo_total:int = area_total/64 * 30
    segundos = tempo_total % 60
    minutos = (tempo_total / 60) % 60
    horas = (tempo_total / 60) / 60


    return int(tempo_total)





