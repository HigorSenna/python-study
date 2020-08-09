"""
Dicionario Comprehension
"""

# Exemplo

numeros = {'a': 1, 'b': 2, 'c': 3}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

lista = [1, 2, 3, 4, 5, 6, 7, 8]
quadrado_dicionario = {'valor' + str(valor): valor ** 2 for valor in lista}
print(quadrado_dicionario)


# Exemplo com condicional

res = {chave: ('par' if valor % 2 == 0 else 'impar') for chave, valor in numeros.items()}
print(res)
