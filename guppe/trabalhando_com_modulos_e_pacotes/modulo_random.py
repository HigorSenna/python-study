"""
Modulo Random

- Em python, modulos nada mais são do que outros arquivos python

Modulo Random -> possui varios funções para geração de números pseudo-aleatórios.
"""

# OBS: Existem duas formas de se utilizar um modulo ou função deste

# Forma 1 - importando todo o modulo (Não recomendado)

import random

# OBS: Ao realizar o import de todo o modulo, todas as funções, classes, atributos e propriedades
# que estiverem dentro do modulo ficarão em memória.

# Neste caso, todas as funcoes a serem utilizadas necessitam do prefixo random, ex: random.seed(), random.random()

# ===============================================================================================================

# Forma 2 - Importando funcao especifica do modulo

# Neste caso, as funcoes a serem utilizadas NÃO necessitam do prefixo random, ex: seed(), random()

from random import random, uniform, randint, choice, shuffle

print(random())  # Gera valores entre 0 e 1

print(uniform(3, 10))  # Gera numeros pseudo-aleatorios entre os valores especificados, 10 não é incluido

print(randint(1, 5))  # Gera numeros INTEIROS pseudo-aleatorios entre os valores especificados, pode gerar 1 e 5

print(choice(['pedra', 'papel', 'tesoura']))  # Mostrar um valor aleatorio em um iteravel
print(choice('Teste'))

lista = ['K', 'Q', 'J', 'A', '2']
print(lista)
shuffle(lista)  # Embaralha dados
print(lista)
