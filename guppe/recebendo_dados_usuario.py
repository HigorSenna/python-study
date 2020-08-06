"""
Recebendo dados do usuario

input() => qualquer dado recebido via input é uma string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Teste'
- Aspas duplas -> "Teste"
- Aspas simples -> triplas '''Teste'''
"""
# - Aspas dupls triplas -> """ Teste """


# print("Qual seu nome? ")
# nome = input()

nome = input("QUal seu nome")

# Exemplo de print 'antigo', versão 2.x
# print("Seja bem vindo %s" % nome)

# Exemplo python 3.x
# print("Seja bem vindo {0}".format(nome))
# Exemplo python 3.7

print(f'Seja bem vindo(a) {nome}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input("Qual sua idade? "))

# Exemplo de print 'antigo', versão 2.x
# print('O %s tem %s anos' % (nome, idade))

# Exemplo python 3.x
# print("O {0} tem {1} anos".format(nome, idade))

# Exemplo python 3.7

print(f'O {nome} tem {idade} anos')

# => int(idade) convert string para int
# print(f'O {nome} nasceu em {2020 - int(idade)}')
print(f'O {nome} nasceu em {2020 - idade}')

