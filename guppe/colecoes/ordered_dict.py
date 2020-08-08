"""
Modulo Collections - Ordered Dict

- Garante a ordem de inserção dos elementos eu um dicionario
"""

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # -> True, já que a ordem dos elementos nao importa para o dicionário comum

# Utilizando

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # -> FALSE, já que a ordem dos elementos importa para o dicionário comum
