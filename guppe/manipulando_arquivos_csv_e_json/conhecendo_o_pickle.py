"""
Conheçendo o Pickle

A função do Picke é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Ou seja: Serialização e Deserialização

#OBS: O Módulo Pickle não é seguro contra dados maliciosos, sendo assim não é recomendado
trabalhar com arquivos pickle vindo de outras pessoas que você nao conheça ou de fontes desconhecidas

"""

import pickle

from typing import List


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.nome} está comendo.')

    @property
    def nome(self):
        return self.__nome


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'{self.nome} está latindo')


cachorro = Cachorro('Pluto')
cachorro2 = Cachorro('Thor')
cachorro3 = Cachorro('Zeus')

# Escrevendo em arquivos pickle
with open('animais.pickle', 'wb') as arquivo:  # wb (w -> write, b-> binary)
    pickle.dump((cachorro, cachorro2, cachorro3), arquivo)


# Lendo em arquivos pickle

with open('animais.pickle', 'rb') as arquivo:  # wb (r -> read, b-> binary)
    cachorros: List[Cachorro] = pickle.load(arquivo)
    print(cachorros)
    for cachorro in cachorros:
        print(cachorro.nome)
