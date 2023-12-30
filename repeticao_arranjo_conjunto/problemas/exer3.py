# Análise:
#   Determinar quantos reais Pedro deverá usar em um certo período.

# Definição:
#   O controle de gastos de Pedro tem tres componentes(Saldo da conta, gastos ,recebimentos) por isso
#   será repesentado por uma estrutura.

from dataclasses import dataclass

@dataclass
class Conta:
    '''
        Indica as entradas e saidas no saldo da conta.
    '''
    SALDO : float
    GASTOS : list[float]
    RECEBIMENTOS : list[float]


























