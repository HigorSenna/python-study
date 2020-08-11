"""
Sorted

OBS: Não confunda com a função sort de list, pois o sort() so funciona com list, porém o
sorted() funciona com qualquer iterável.

list.sort() -> modifica a propria lista
sorted(iterável) -> retorna a lista ordenada

OBS: Independente do iretavel passado em sorted(), o retorno é SEMPRE do tipo list.

"""

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))  # Orderna em ordem CRESCENTE

# Adicionando parâmetros

print(sorted(numeros, reverse=True))  # Ordena em ordem DECRESCENTE

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "amarelo", "musica": "rock"}
]

print(usuarios)

# Ordenando pelo username - Ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario.get('username')))


# Ordenando pelo numero de tweets - Crescente
print(sorted(usuarios, key=lambda usuario: len(usuario.get('tweets'))))

