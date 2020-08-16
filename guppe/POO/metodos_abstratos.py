"""
Métodos Abstratos
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    # Declarando método abstrato
    def falar(self):
        raise NotImplementedError('A Classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print('Falando como cachorro')

