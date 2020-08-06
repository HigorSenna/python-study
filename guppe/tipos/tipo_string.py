"""
Tipo String

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
#  [ 0,   1,   2,    3,    4,    5,    6,   7,   8,  9,   10,  11,  12,  13 ]
#  ['A', 'n', 'g' , 'e' , 'l' , 'i' , 'n', 'a', '', 'J', 'o', 'l', 'i', 'e' ]
nome = 'Angelina Jolie'
print(nome)

nome2 = 'Angelina \nJolie'
print(nome)
nome = """ Angelina
Jolie
"""
print(nome)
print(nome[0:4])  # printa os caracteres de 0 a 4

print(nome.split()[0])  # Printa o nome antes do primeiro espaco
print(nome.split()[1])  # Printa o nome antes do segundo espaco

"""
Comece do primeiro elemento, vá até o ultimo elemento e inverta
"""
print(nome[::-1])

print(nome.replace('A', 'I'))
