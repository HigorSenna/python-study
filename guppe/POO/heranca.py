"""
Herança
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # Cliente Herdando de pessoa

    def __init__(self, nome, sobrenome, cpf, renda):

        super().__init__(nome, sobrenome, cpf)
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma nao comum de acessar dados da classe pai

        self.__renda = renda


class Funcionario(Pessoa):  # Funcionario Herdando de pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):

        super().__init__(nome, sobrenome, cpf)
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma nao comum de acessar dados da classe pai

        self.__matricula = matricula

    # Sobrescrevendo método da classe pai (Override)
    def nome_completo(self):
        return f'Funcionário: {super().nome_completo()}'


cliente = Cliente('Higor', 'Senna', '123.456.789-10', 10)
funcionario = Funcionario('Higor', 'Senna', '123.456.789-10', 1234)

print(funcionario.nome_completo())
print(cliente.nome_completo())
