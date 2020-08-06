"""
Tipo numerico float

Tipo real, decimal

Casas decimais
"""

# Errado do ponto de vista do Float, mas gera um tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuicao
valor1, valor2 = 1, 44  # Os valores vao para as respectivas variáveis, na ordem
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, perdemos precisão
"""
resultado = int(valor)
print(resultado)
print(type(resultado))

# É possivel trabalhar com numeros complexos
variavel = 5j
print(type(variavel))
