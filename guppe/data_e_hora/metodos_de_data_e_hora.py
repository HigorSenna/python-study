"""
Métodos de data e hora
"""

import datetime

print(datetime.datetime.now())  # Podemos especificar o timezone
print(datetime.datetime.today())  # Nao conseguimos especificar o timezone


# Mudanças ocorrendo a Meia Noite do proximo dia

horario_zerado = datetime.time()
data_atual = datetime.datetime.now()
amanha = data_atual + datetime.timedelta(days=1)

manutencao = datetime.datetime.combine(amanha, horario_zerado)
print(manutencao)

# Dia da semana
# 0 - Segunda
# 1 - Terça
# 2 - Quarta
# 3 - Quinta
# 4 - Sexta
# 5 - Sábado
# 6 - Domingo

print(datetime.datetime.now().weekday())

# Formatando

print(datetime.datetime.now().strftime('%d/%m/%Y %H:%m:%S'))

# pip install textblob

from textblob import TextBlob

# Método translate necessita de internet


def formatar_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')}"


print(formatar_data(datetime.datetime.now()))

# Convertendo String para Date

nasc = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nasc)
print(nasc.strftime('%d/%m/%Y'))

# Somente hora

horario_almoco = datetime.time(12, 30, 0)
print(horario_almoco)

# Marcando tempo de execução do nosso codigo

import timeit, functools

tempo = timeit.timeit('"qualquer".join("outra")', number=10000)
print(tempo)


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma += num * 4
    return soma


tempo_execucao = timeit.timeit(functools.partial(teste, 4), number=60000000)
print(tempo_execucao)
