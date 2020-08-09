"""
List Comprehension

- Podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe

[dados for dado in iterável]

"""

#   Exemplos

numeros = [1, 2, 3, 4, 5]
resposta = [numero * 10 for numero in numeros]

print(resposta)


def manipular(numero):
    return numero + 1


resposta2 = [manipular(numero) for numero in numeros]
print(resposta2)


# List Comprehensions vs Loop convencional

# Loop convencional

numeros_dobrados = []

for numero in numeros:
    numero *= 2
    numeros_dobrados.append(numero)

print(numeros_dobrados)


# List Comprehension

print([numero * 2 for numero in numeros])


letras = 'Teste'

print([letra.upper() for letra in letras])

amigos = ['maria', 'julia', 'pedro', 'jose']

print([amigo.title() for amigo in amigos])
