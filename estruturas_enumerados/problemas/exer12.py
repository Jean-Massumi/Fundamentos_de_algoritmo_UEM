# Análise:
#   Certa sala de reunião pode ser usada das 8:00h ás 18:00h , verifique se duas reservas podem ser atendidas
#   sem que haja conflitos de horário.

# Definição:
#   O inicio e o termino da reuniao serao representado por valores float positivos.

from dataclasses import dataclass

@dataclass
class Reservas:
    '''
        Intervalo de tempo de uma reuniao.
    '''
    INICIO : float
    FIM : float

def verificar_reservas(r1:Reservas, r2:Reservas) -> str:
    '''
        Verificar se duas reservas podem ser atendidas, sem que haja conflito de horario entre elas.

        A reserva da sala deve está entre os horários das 8:00h ás 18:00h.
    
    >>> verificar_reservas(Reservas(9, 12),Reservas(13, 15))
    'As reservas podem ser atendidas!'
    >>> verificar_reservas(Reservas(8, 9),Reservas(9, 11))
    'As reservas podem ser atendidas!'
    >>> verificar_reservas(Reservas(16, 18),Reservas(15, 16))
    'As reservas podem ser atendidas!'
    >>> verificar_reservas(Reservas(8, 11),Reservas(9, 10))
    'As reservas foram Negadas! Pois a conflitos de horario.'
    >>> verificar_reservas(Reservas(12, 15),Reservas(11, 13))
    'As reservas foram Negadas! Pois a conflitos de horario.'
    >>> verificar_reservas(Reservas(8.30, 10.30),Reservas(10.30, 12.45))
    'As reservas podem ser atendidas!'
    >>> verificar_reservas(Reservas(10.15, 11.30),Reservas(8.45, 11))
    'As reservas foram Negadas! Pois a conflitos de horario.'
    >>> verificar_reservas(Reservas(12.15, 13.15),Reservas(13.14, 15))
    'As reservas foram Negadas! Pois a conflitos de horario.'
    >>> verificar_reservas(Reservas(12.10, 13.30),Reservas(9.40, 11.45))
    'As reservas podem ser atendidas!'
    >>> verificar_reservas(Reservas(11.27, 15.23),Reservas(15.24, 16.45))
    'As reservas podem ser atendidas!'
    '''

    if r1.FIM <= r2.INICIO or r1.INICIO >= r2.FIM:
        verificacao = 'As reservas podem ser atendidas!'
    else:
        verificacao = 'As reservas foram Negadas! Pois a conflitos de horario.'

    return verificacao






















