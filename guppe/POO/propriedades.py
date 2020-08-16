"""
Propriedades
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def mostrar_extrato(self):
        return f'Saldo de {self.__saldo} so cliente {self.__titular}'

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    # podemos criar qualquer metodo e declara-lo como propriedade

    @property
    def total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Higor', 3000, 5000)
conta2 = Conta('Senna', 2000, 4000)

print(conta1.__dict__)
conta1.limite = 900000
print(conta1.__dict__)
print(conta1.total)

