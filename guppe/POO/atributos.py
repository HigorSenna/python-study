"""
Atributos

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe deve ser PUBLICO, caso queira colocar
privado, é so usar __ em sua declaracao

"""

# Classe com atributos privados


class Lampada:

    # OBS: Atributos privados: __nome
    def __init__(self, voltagem, cor):  # Construtor
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha


acesso = Acesso('email@gmail.com', '123456')
print(acesso.email)
# print(acesso.__senha) # AtributeError

# Name Mangling -> conseguimos acessar um atributo mesmo sendo privado (nao recomendado)
print(acesso._Acesso__senha)


# Classe com atributos publicos

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


# Em python, o primeiro atributo de um método é sempre a referencia do objeto, e como convenção sempre devemos chama-lo
# de self, porém podemos colocar qualquer nome:

class ContaPoupanca:
    def __init__(this, numero, limite, saldo):
        this.numero = numero
        this.limite = limite
        this.saldo = saldo


# ATRIBUTOS DE CLASSE (em Java: static)
from random import random


class Produto:

    imposto = 1.05  # Atributo de instancia

    def __init__(self, nome, valor):
        self.id = random()
        self.nome = nome
        self.valor = (valor * Produto.imposto)


p1 = Produto('PS4', 2300)

print(p1.imposto)  # Acesso possivel más incorreto para acesso ao atributo de classe, forma correta:
print(Produto.imposto)

p2 = Produto('PS5', 6000)


# Atributos Dinâmicos (Não comum)
# - É um atributo de instância que pode ser criado em tempo de execução e será exclusivo da instância que o criou

p3 = Produto('Xbox', 2300)
p3.peso = '5Kg'  # Note que na classe produto nao existe o atributo peso
print(p3.peso)

# Listando os objetos com seus respectivos valores:

print(p3.__dict__)  # Pega os atributos de INSTÂNCIA com seus valores e transforma e retorna um dicionario

# Deletando atributos

del p3.peso
print(p3.__dict__)

del p3.nome
print(p3.__dict__)  # Posso deletar qualquer atributo de instância
