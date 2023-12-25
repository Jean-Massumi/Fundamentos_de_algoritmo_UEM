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
    
    >>> verificar_reservas(Reservas(9,12),Reservas(13,15))
    'As reservas podem ser atendidas!'
    >>> verificar_reservas(Reservas(8,9),Reservas(9,11))
    'As reservas podem ser atendidas!'



    '''

    
























