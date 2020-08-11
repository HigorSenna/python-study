"""
Min e Max

max() -> retorna o menor valor em um iterável ou o maior de dois ou mais elementos
min() -> retorna o menor valor em um iterável ou o menor de dois ou mais elementos
"""

lista = [1, 8, 4, 9, 128]
print(max(lista))

tupla = 1, 8, 4, 9, 128
print(max(tupla))

set = {1, 8, 4, 9, 128}
print(max(set))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 9, 'e': 128}
print(max(dicionario.values()))

num1 = 5
num2 = 89
num3 = 100

print(max(num1, num2))
print(max(num1, num2, num3))  # quantidade de numeros ilimitada
print(max('QualquerString'))

# ==============================================================

lista = [1, 8, 4, 9, 128]
print(min(lista))

tupla = 1, 8, 4, 9, 128
print(min(tupla))

set = {1, 8, 4, 9, 128}
print(min(set))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 9, 'e': 128}
print(min(dicionario.values()))

num1 = 5
num2 = 89
num3 = 100

print(min(num1, num2))
print(min(num1, num2, num3))  # quantidade de numeros ilimitada
print(min('QualquerString'))

# ==============================================================

nomes = ['Arya', 'Samsom', 'Droa', 'Tim', 'Olivvander']
print(max(nomes))  # Ordem alfabetica maior para menor
print(min(nomes))  # Ordem alfabetica menor para maior

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))


usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "amarelo", "musica": "rock"}
]

print(max(usuarios, key=lambda usuario: usuario.get('username')))
print(min(usuarios, key=lambda usuario: usuario.get('username')))

# Imprimir apenas o nome
max_nome = max(usuarios, key=lambda usuario: usuario.get('username'))
print(f"O nome é {max_nome.get('username')}")

# Pegando o menor nome por ordem alfabetica manualmente
menor_nome = ''
for elemento in usuarios:
    if menor_nome == '':
        menor_nome = elemento.get('username')
    else:
        if elemento.get('username')[0] < menor_nome[0]:
            menor_nome = elemento.get('username')

print(menor_nome)
