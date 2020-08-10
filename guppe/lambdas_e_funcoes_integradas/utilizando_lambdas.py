"""
Utilizando Lambdas

- Funcoes anônimas

"""

multiplicar = lambda x: 3 * x + 1
print(multiplicar(3))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('   teste', 'tESTANDO'))

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Eric Ries',
           'Orson Scott Card', 'Douglas Adams']

print(autores)


# Forma mais comum da utilizacao da lamdas em python, usando-a diretamento onde necessário
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


def funcao_quadratica(a, b, c):
    return lambda x: (a * (x ** 2)) + (b * x) + c


print(funcao_quadratica(2, 3, -5)(2))

calcular = funcao_quadratica(2, 3, -5)
print(calcular(2))
