"""
Metodo super()
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    @property
    def nome(self):
        return self.__nome


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)  # Acessando o contrutor da classe pai
        self.__raca = raca


gato = Gato('Frajola', 'Felino', 'Angorá')
print(gato.nome)
