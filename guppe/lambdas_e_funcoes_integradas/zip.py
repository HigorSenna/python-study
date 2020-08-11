"""
Zip

zip() -> cria um iteravel chamado (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada
em pares
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)  # OBS: Após utilizar a função zip, depois da primeira utilização do resultado, ele zera
print(type(zip1))

zip1 = zip(lista1, lista2)
print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))


lista3 = [7, 8, 9, 10, 11]

# OBS: O zip utiliza como parametro o menor tamanho como iteravel, isso significa que se estiver trabalhando
# com iteraveis de tamanhos diferentes, irá parar quando os elementos de menor iterável acabar

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

tupla = 1, 2, 3, 4, 5
dicionario = {'a': 11, 'b': 12, 'c': 13}

zt = zip(tupla, lista1, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))


prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(list(zip(alunos, prova1, prova2)))
print(final)

# Podemos utilizar map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print("=========================")
print(list(zip(prova1, prova2)))
print(list(map(lambda nota: max(nota), zip(prova1, prova2))))
print("=========================")
print(dict(final))
