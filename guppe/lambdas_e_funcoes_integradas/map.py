"""
Map

 - Com map, fazemos mapeamento de valores para funcao.
"""

import math


def calcular_area(r):
    """ Calcula a área de um circulo de raio 'r' """
    return math.pi * (r ** 2)


print(calcular_area(2))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Froma comum

areas = []

for r in raios:
    areas.append(calcular_area(r))

print(areas)

# Com Map

areas = map(calcular_area, raios)
print(type(areas))
print(list(areas))

# Map com Lambda

areas = map(lambda raio: math.pi * (raio ** 2), raios)
print(list(areas))
print(list(areas))  # OBS: Após utilizar a função map, depois da primeira utilização do resultado, ele zera

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]
print(cidades)

# f = 9/5 * c + 32

converter_temperatura = lambda dado: (dado[0], str((9/5) * dado[1] + 32) + 'F')

temperaturas_convertidas = map(converter_temperatura, cidades)
print(tuple(temperaturas_convertidas))
