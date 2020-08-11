"""
Reversed

OBS: nao confunda com a funcao reverse() que utilizamos na lista

A funcao .reverse() so funciona em listas, ja a funcao em reversed() funciona com qualquer iteravel,
sua funcao é inverter o iteravel

A funcao reversed() retorna um iteravel chamado List Reverse Iterator
"""

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(type(res))
print(list(res))

tupla = 1, 2, 3, 4, 5
res = reversed(tupla)
print(type(res))
print(list(res))

set1 = {1, 2, 3, 4, 5}
# res = reversed(set1)c # Nao funciona pois o set nao tem ordwem

for n in reversed(range(0, 10)):
    print(n)



