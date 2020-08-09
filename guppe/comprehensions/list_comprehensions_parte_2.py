"""
List Comprehension Parte 2

 - Podemos adicionar estruturas condicionais nas list comprehensions
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


pares = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(pares)
