"""
Tuplas

As tuplas sao parecidas com listas.

OBS: Por serem imutaveis, tuplas são mais rápidas que listas no quesito performance

OBS: Na tupla nao temos Shallow Copy

Diferenças básicas:

1 - As tuplas são representadas por parênteses (), porem elas podem ser criadas de duas formas:
  Forma 1: tupla1 = (1, 2, 3, 4)
  Forma 2: tupla2 = 1, 2, 3, 4

2 - As tuplas são IMUTÁVEIS, toda operação em uma tupla, gera uma nova tupla.

Métodos para ADIÇÃO e REMOÇÃO nao existem para tuplas, pois são imutaveis
"""

tupla1 = (1, 2, 3, 4)

tupla2 = 1, 2, 3, 4

# CUIDADO com tupla de 1 elemento

tupla3 = (4)  # Isso NÃO é uma tupla
tupla4 = (4,)  # Isso é uma tupla
tupla5 = 4,  # Isso é uma tupla

# Gerando tupla a partir do range

tupla6 = tuple(range(11))

# Desempacotamento de tupla
# Se tivermos mais elementos para desempacotar do que variaveis para receber ou vice-versa, teremos ValueError

tupla7 = 'Elemento1', 'Elemento2'
elemento1, elemento2 = tupla7

# Soma, Valor Maximo, Valor Minimo -> Apenas se todos os valores forrem numeros inteiros ou reais

tupla8 = 1, 2, 3, 4, 5, 60
print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

# Concatenação de tuplas

print(tupla4 + tupla5)

# Encontrar valores dentro da tuplas
print(5 in tupla8)

# Iterando na tupla

for valor in tupla8:
    print(valor)

i = 0
while i < len(tupla8):
    print(tupla8[i])
    i += 1

# Contando elementos
tupla9 = 'a', 'b', 'c', 'a', 'd'
tupla9.count('a')

# Obtendo o index do elemento
tupla9.index('a')  # Caso o elemento nao exista, será gerado ValueError

# Slicing
print(tupla9[::])
print(tupla9[1:2:2])
print(tupla9[::-1])  # Invertendo a tupla

# OBS: a tupla tem todos os metodos que contem na lista, com exceção dos metodos de remoção e adição
