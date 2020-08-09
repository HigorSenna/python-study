"""
Modulo Collections - Named Tuple

 - São tuplas diferenciadas onde especficiamos um nome para a mesma e parâmetros
"""

# Utilizando

from collections import namedtuple

# Declaraçoes
cachorro = namedtuple('cachorro', 'idade raca nome')
# ou
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')
# ou
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)
print(ray[0])
# ou
print(ray.idade)

