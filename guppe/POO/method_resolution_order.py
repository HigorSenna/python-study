"""
Method Resolution Order (MRO)

Em Python, podemos conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

    @property
    def nome(self):
        return self.__nome


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self.nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou {self.nome} da terra!'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


pinguim = Pinguim('Tux')


# Pinguim(Aquatico, Terrestre):
# # Eu sou Tux do mar!

# Method Resolution Order (MRO) -> executa o método comum(cumprimentar) da primeira classe herdada, no caso Terrestre.
# Pinguim(Terrestre, Aquatico):
# Eu sou Tux da terra!
print(pinguim.cumprimentar())


print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))

