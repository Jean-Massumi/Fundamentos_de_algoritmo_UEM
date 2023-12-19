from dataclasses import dataclass

@dataclass
class Tempo:
    horas : int
    minutos : int
    segundos : int

def segundos_para_tempo(segundos:int) -> Tempo:
    '''
    Exemplos:
    >>> segundos_para_tempo(160)
    Tempo(horas=0, minutos=2, segundos=40)
    >>> segundos_para_tempo(3760)
    Tempo(horas=1, minutos=2, segundos=40)

    '''

    h = segundos // 3600
    restante = segundos % 3600
    m = restante // 60
    s = restante % 60

    return Tempo(h, m, s)

def tempo_para_string(t: Tempo) -> str:
    '''
    Converte *t* em uma mensagem para o usuário. Cada componente de *t* aparece
    com a sua unidade, mas se o valor do componente for 0, ele não aparece na
    mensagem. Os componentes são separados com "e" ou "," respeitando as regras
    do Português. Se *t* for Tempo(0, 0, 0), devolve "0 segundo(s)".

    Exemplos
    >>> # horas == 0 and minutos == 0
    >>> tempo_para_string(Tempo(0, 0, 0))
    '0 segundo(s)'
    >>> tempo_para_string(Tempo(0, 0, 1))
    '1 segundo(s)'
    >>> tempo_para_string(Tempo(0, 0, 10))
    '10 segundo(s)'

    >>> # horas == 0 and minutos != 0 \
    >>> #            and segundos != 0
    >>> tempo_para_string(Tempo(0, 1, 20))
    '1 minuto(s) e 20 segundo(s)'

    >>> # horas == 0 and minutos != 0 \
    >>> #            and segundos == 0
    >>> tempo_para_string(Tempo(0, 2, 0))
    '2 minuto(s)'

    >>> # horas != 0 and minutos != 0 and segundos != 0
    >>> tempo_para_string(Tempo(1, 2, 1))
    '1 hora(s), 2 minuto(s) e 1 segundo(s)'

    >>> # horas != 0 and minutos == 0 and segundos != 0
    >>> tempo_para_string(Tempo(4, 0, 25))
    '4 hora(s) e 25 segundo(s)'

    >>> # horas != 0 and minutos != 0 and segundos == 0
    >>> tempo_para_string(Tempo(2, 4, 0))
    '2 hora(s) e 4 minuto(s)'

    >>> # horas != 0 and minutos == 0 and segundos == 0
    >>> tempo_para_string(Tempo(3, 0, 0))
    '3 hora(s)'
    '''
    h = str(t.horas) + ' hora(s)'
    m = str(t.minutos) + ' minuto(s)'
    s = str(t.segundos) + ' segundo(s)'
    # Temos 7 formas distintas
    if t.horas > 0:
        if t.minutos > 0:
            if t.segundos > 0:
                msg = h + ', ' + m + ' e ' + s
            else:
                msg = h + ' e ' + m
        elif t.segundos > 0:
            msg = h + ' e ' + s
        else:
            msg = h
    elif t.minutos > 0:
        if t.segundos > 0:
            msg = m + ' e ' + s
        else:
            msg = m
    else:
        msg = s
    return msg


















