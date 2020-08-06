"""
Estrutura de repeticao 'For'

Exemplos de itaraveis

- String
   nome = 'Teste'
- Lista
   lista = [1, 2, 3]
- Range
   numeros = range(1, 10)

"""

nome = 'Teste'
lista = [1, 2, 3]
numeros = range(1, 3)  # temos que transformar em uma lista

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

"""
range(valo_inicial, valor_final)
OBS: O valor final não é inclusive.
range(1, 3)
1
2
3 - Não
"""
for numero in numeros:
    print(numero)

"""
Enumerate, retorna um indice,valor de cada elemento
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

"""
No python quando eu tenho dois parâmetros e vou usar só um, 
posso user o _ (underline) para descartar o parâmetro
"""
for _, letra in enumerate(nome):
    print(letra)

for enumerated in enumerate(nome):
    print(enumerated)

quantidade = int(input('Quantars vezes o loop deve rodar?'))
for n in range(1, quantidade + 1):
    print(f'Imprimindo {n}')

# Imprimir sem pular linha
for n in range(1, quantidade + 1):
    print(f' Imprimindo {n}', end='')


# No python é possivel multiplicar strings
nome = 'Teste '
print(nome * 5, end='')

emoji = '\U0001F60D'
print(emoji)
