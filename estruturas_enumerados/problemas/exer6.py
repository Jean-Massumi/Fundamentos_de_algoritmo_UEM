# Análise:
#   Calcular o valor final que o consumidor tem que pagar dado o seu consumo em kilowatts/hora , a tarifa
#   básica do kilowatt/hora e a bandeira tarifária.

# Definição:
#   A bandeira tarifária possui 4 tipos de bandeiras:
#       Bandeira Verde indica condições favoráveis , então a tarifa não sofre acréscimo.
#       Bandeira Amarela indica condições menos favoráveis, então a tarifa sofre um acréscimo de R$0,01874 Kw/h.
#       Bandeira Vermelha1 indica condições mais custosas, então a tarifa sofre um acréscimo de R$0,03971 Kw/h.
#       Bandeirad Vermelha2 indica condições ainda mais custosas, então a tarifa sofre um acréscimo de 
#       R$0,09492 por cada Kw/h consumido.

#   A tarifa básica e o consumo de kilowatt serão representados por valores float.
#   A bandeira tarifária será representado por uma string.

from dataclasses import dataclass

@dataclass
class Consumidor:
    CONSUMO_KwH : float
    TARIFA_BASICA : float
    BANDEIRA_TARIFARIA : str


def calcular_consumo(valor:Consumidor) ->float:
    '''
        Calcular o valor final que o consumidor tem que pagar dado o seu consumo em kilowatts/hora , a tarifa
    básica do kilowatt/hora e a bandeira tarifária.

        Se a *bandeira* for VERDE indica condições favoráveis , então a tarifa não sofre acréscimo.
        Se a *bandeira* for AMARELA indica condições menos favoráveis, então a tarifa sofre um acréscimo
    de R$0,01874 Kw/h.
        Se a bandeira for VERMELHA_1 indica condições mais custosas, então a tarifa sofre um acréscimo 
    de R$0,03971 Kw/h.
        Se a bandeira for VERMELHA_2 indica condições ainda mais custosas, então a tarifa sofre um acréscimo
    de R$0,09492 por cada Kw/h consumido.

    Exemplos:
    >>> calcular_consumo(Consumidor(152.2, 0.3, 'VERDE'))
    45.66
    >>> calcular_consumo(Consumidor(191.9, 0.3, 'AMARELO'))
    61.17
    >>> calcular_consumo(Consumidor(233.4, 0.3, 'VERMELHO_1'))
    79.29
    >>> calcular_consumo(Consumidor(287.1, 0.3, 'VERMELHO_2'))
    113.38
    '''

    if valor.BANDEIRA_TARIFARIA == 'VERDE':
        valor_final = valor.CONSUMO_KwH * (valor.TARIFA_BASICA)
    elif valor.BANDEIRA_TARIFARIA == 'AMARELO':
        valor_final = valor.CONSUMO_KwH * (valor.TARIFA_BASICA + 0.01874)
    elif valor.BANDEIRA_TARIFARIA == 'VERMELHO_1':
        valor_final = valor.CONSUMO_KwH * (valor.TARIFA_BASICA + 0.03971)
    else:
        valor_final = valor.CONSUMO_KwH * (valor.TARIFA_BASICA + 0.09492)

    return round(valor_final,2)






















