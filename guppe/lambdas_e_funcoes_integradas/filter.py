"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção

"""

valores = 1, 2, 3, 4, 5, 6
media = sum(valores) / len(valores)
print(media)

import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados
media = statistics.mean(dados)
print(f'Média: {media}')

# Cada item de dados é passado como parâmetro da expressao lambda
res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))  # OBS: Após utilizar a função filter, depois da primeira utilização do resultado, ele zera
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', '', 'Colombia', 'Equador', '', '', 'Venezuela']
print(paises)

res_paises = filter(lambda pais: len(pais) > 0, paises)  # Remove os itens vazios
print(list(res_paises))

res_paises = filter(None, paises)  # Remove os itens vazios
print(list(res_paises))

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

usuarios_inativos = filter(lambda usuario: len(usuario.get('tweets')) == 0, usuarios)
print(list(usuarios_inativos))

usuarios_inativos = filter(lambda usuario: not usuario.get('tweets'), usuarios)
print(list(usuarios_inativos))


# Combinando filter e map

nomes = ['Vanessa', 'Ana', 'Maria']


# Criar uma lista com nomes que tem menos de 5 caracteres

instruturas = map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes))
print(list(instruturas))
