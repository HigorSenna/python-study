"""
Herança Multipla

OBS: A herança multipla pode ser feita de duas maneiras:
   - Por Multiderivação Direta;
   - Por Multiderivação Indireta;

Multiderivação Direta e Multiderivação Indireta não tem diferença de comportamento é apenas um conceito;
"""


class Base1:
    pass


class Base2:
    pass


# Multiderivação Direta
class MultiderivadaDireta(Base1, Base2):  # Posso herdar quantas classes necessitar
    pass


# Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


# Multiderivação Indireta
class MultiderivadaIndireta(Base2):  # Posso herdar quantas classes necessitar
    pass


# =====================================================================================

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


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Tux')
print(pinguim.andar())
print(pinguim.nadar())

# Method Resolution Order (MRO) -> executa o método comum(cumprimentar) da primeira classe herdada, no caso Terrestre.
print(pinguim.cumprimentar())

print(f'Objeto é uma instancia de pinguim? {isinstance(pinguim, Pinguim)}')
print(f'Objeto é uma instancia de pinguim? {isinstance(pinguim, str)}')

# Toda classe de python herda de object por default
print(f'Objeto é uma instancia de pinguim? {isinstance(pinguim, object)}')
