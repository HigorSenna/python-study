"""
Ranges sao utilizados para gerar sequencias numeros
de maneiras especificada

Formas gerais:

range(valor_de_parada)
OBS: valor_de_parada nao inclusive(inicio padrao 0, e passo de um em 1)

range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada nao inclusive(inicio padrao 0, e passo de um em 1)

range(valor_inicio, valor_de_parada, passo)
OBS: valor_de_parada nao inclusive(inicio padrao 0, e passo especificado pelo usuario)

(inverso, passo negativo)
range(valor_inicio, valor_de_parada, passo)
OBS: valor_de_parada nao inclusive(inicio padrao 0, e passo especificado pelo usuario)
"""

for num in range(11):
    print(' ', end='')
    print(num, end='')

print(' ')
for num in range(2, 11):
    print(' ', end='')
    print(num, end='')

print(' ')
for num in range(1, 11, 2):
    print(' ', end='')
    print(num, end='')

print('')
for num in range(10, 1, -1):
    print(' ', end='')
    print(num, end='')

print('')
# Converter range para lista

lista = list(range(1, 10))
print(lista, end='')

