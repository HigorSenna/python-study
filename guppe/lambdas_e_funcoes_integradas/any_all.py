"""
Any e All

all() -> Retorna true se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio
# OBS: Um iteravel vazio convertido em bool é False, mas o All considera True

any() -> Retorna True se qualquer elemento for verdadeiro. Se o iterável estiver vazio, retorna False
"""

# Em python, qualquer numero != 0 é True
# Em python, qualquer letra é True

print(all([1, 2, 3, 4]))
print(all([0, 1, 2, 3, 4]))
print(all([]))
print(all(''))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano']
print(all(nome[0] == 'C' for nome in nomes))

print(all(letra for letra in 'eio' if letra in 'aeiou'))

print(any([0, 1, 2, 3, 4]))
print(any([0, False, {}, (), []]))
print(any(nomes))
