"""
Listas Python

Listas em python funcionam como arrays, com a diferença
de serem dinamicos e tambem de podermos colocar QUALQUER tipo de dado

OBS:
- Dinâmico: Não possuem tamanho fixo; Ou seja podemos criar a lista
e simplesmente ir adicionando elementos; (enquanto estiver memória disponível)

- Qualquer tipo de dado: Nao possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado
na mesma lista.
"""

type([])

lista1 = [1, 2, 3, 4, 5, 99, 23, 42, 15, 99]
lista2 = ['G', 's', 'L']
lista3 = []
lista4 = list(range(11))
lista5 = list('Teste')

#  Facilmente encontrando se um elemento está na lista
if 8 in lista4:
    print('Encontrei o 8')
else:
    print('Nao encontrei o 8')

#  Ordenar lista

lista1.sort()
print(lista1)

#  Contar numero de ocorrencias de um valor em uma lista
print(lista1.count(99))

#  Adicionar elementos

lista1.append(42)  # append só adiciona um elemento por vez

#  Adicionando uma lista dentro de  outra lista
lista1.append([8, 3, 1])

# Econtrando uma lista dentro de outra lista

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('ao encontrei a lista')

#  Coloca cada elementro passado como valor adicional da lista.. (Nao vira uma lista dentro da lista)
lista1.extend([123, 44, 67])

#  Inserir elemento na lista informando a posicao do indice
#  Nao subistitui o valor anterior que estava na posicao do indice, ele 'ele é deslocado pra a direita da lista'
lista1.insert(2, 'Novo valor')

#  Juntar listas
lista6 = lista1 + lista2
# ou
lista1.extend(lista2)

#  Inverter lista
lista1.reverse()
# ou
nova_lista_invertida = lista1[::-1]

#  Copiar uma lista
lista7 = lista1.copy()

#  Tamando da lista
len(lista1)

#  Remover ultimo elemento da lista
#  OBS: Remove e retorna o ultimo elemento
lista7.pop()

#  Remover elemento pelo indice
lista5.pop(2)

#  Remover todos os elementos da lista(zerar a lista)
lista8 = lista1.copy()
lista8.clear()

#  Repetir elementos em uma lista
lista9 = lista1.copy()
lista9 *= 3

print(lista9)

#  Converter string para lista
curso = 'Programacao em Python'
curso = curso.split()  # Por padrao o split separa os elementos da lista pelo espaço entre elas
curso2 = 'Programacao,em,Python'
curso2 = curso2.split(',')

#  Converter lista em string
lista10 = ['Programcao', 'em', 'Python']
lista10_string = ' '.join(lista10)  # Coloca o espaco entre cada elemento da lista e transforma em string


#  Iterando em listas
#  Exemplo 1
lista11 = ['Teste', True, 4.456, 489, [1, 2, 3]]

for elemento in lista11:
    print(elemento)

# Exemplo 2
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Fazer acesso aos elementos de forma indexada inversa
"""
Para entender melhor o índice negativo, pensa na lista como um círculo, onde
o final de um elemento está ligado ao inicio da lista
"""

cores = ['Branco', 'Azul', 'Amarelo', 'Verde']
print(cores[-1])  # Verde
print(cores[-2])  # Amarelo
print(cores[-3])  # Azul
print(cores[-4])  # Branco

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Encontrar o indice de um elemento na lista

print(cores.index('Branco'))
# OBS: Caso nao tenha o elemento na lista, será apresentado ValueError

lista_elementos_repetidos = ['Preto', 'Azul', 'Branco', 'Preto', 'Amarelo']
print(lista_elementos_repetidos.index('Preto'))  # Retorna o indice do PRIMEIRO ELEMENTO encontrado

# Buscar indice a partir de um indice especifico
print(lista_elementos_repetidos.index('Preto', 2))  # Busca o indice do elemento 'Preto' a partir do indice 2 da lista

# Buscar indice a partir de um range de indices
# Busca o indice do elemento 'Preto' entre o range do indice 1 a 4
print(lista_elementos_repetidos.index('Preto', 1, 4))

# slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro inicio

lista_slice1 = [1, 2, 3, 4, 5, 6]
print(lista_slice1[1:])  # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro fim
print(lista_slice1[:2])  # começa em 0, pega até o indice 2 - 1, o indice 2 nao é incluido

# Trabalhando com slice de lista com o parâmetro inicio fim
print(lista_slice1[1:4])  # começa em 1, pega até o indice 4 - 1, o indice 4 nao é incluido

# Trabalhando com slice de lista com o parâmetro passo
print(lista_slice1[1::2])  # Começa em 1, vai até o final, de 2 em 2

print(lista_slice1[::2])  # Começa em 0, vai até o final, de 2 em 2

print(lista_slice1[::-1])  # Começa em 0, vai até o final, de traz pra frente

# Soma, Valor Maximo, Valor Minimo -> Apenas se todos os valores forem numeros inteiros ou reais

lista_operacoes = [1, 2, 3, 4, 5, 6, 7]
print(sum(lista_operacoes))  # Soma todos os elementos
print(max(lista_operacoes))  # Pega o maior valor
print(min(lista_operacoes))  # Pega o menor valor

# Converter lista para tupla
tuple(lista_operacoes)

# Desempacotamento de listas
# Se tivermos mais elementos para desempacotar do que variaveis para receber ou vice-versa, teremos ValueError
lista_desempacotar = [1, 2, 3]
var1, var2, var3 = lista_desempacotar

# Copiando uma lista para outra (Shallow copy e Deep Copy)
# Deep copy -> a lista é copiada e as alteracoes feitas na lista copiada nao é refletida na lista original

lista_para_copiar = [1, 2, 3]
print(lista_para_copiar)

nova_lista = lista_para_copiar.copy()

print(nova_lista)

nova_lista.append(4)

print(lista_para_copiar)
print(nova_lista)

# Shallow copy -> a lista é copiada e as alteracoes feitas na lista copiada É refletida na lista original

lista_para_copiar2 = [1, 2, 3]
print(lista_para_copiar2)

nova_lista2 = lista_para_copiar2  # Copia via atribuição

print(nova_lista2)

nova_lista2.append(4)

print(lista_para_copiar2)
print(nova_lista2)
