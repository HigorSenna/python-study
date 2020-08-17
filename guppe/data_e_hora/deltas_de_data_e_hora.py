"""
Trabalhando com deltas de data e hora

Diferença de data inicial e data final (delta)

"""

import datetime

hoje = datetime.datetime.now()
niver = datetime.datetime(2021, 3, 3, 0)

# Calculando o delta
tempo_para_evento = niver - hoje

print(tempo_para_evento)

# Somando 3 dias

nova_data = datetime.datetime.now() + datetime.timedelta(days=3)
print(nova_data)