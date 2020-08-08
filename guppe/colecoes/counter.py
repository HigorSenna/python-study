"""
Modulo de Collections - Counter

Counter -> Recebe um iteravel como parâmetro e cria um objeto do tipo Collections Counter, ele é PARECIDO
com um dicionário

"""

# Utilizando o counter

from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 5, 5, 5, 45, 45]
res = Counter(lista)
print(res)  # Counter({1: 3, 3: 3, 5: 3, 2: 2, 45: 2})
# Para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrencias

print(type(res))

print(Counter('Teeeste'))  # Counter({'e': 4, 'T': 1, 's': 1, 't': 1})

texto = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard
dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen
book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release
of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
PageMaker including versions of Lorem Ipsum.
"""

palavras = texto.split()
print(palavras)
res2 = Counter(palavras)
print(res2)

#  Encontrando as 5 palavras com mais ocorrencias no texto
print(res2.most_common(5))
