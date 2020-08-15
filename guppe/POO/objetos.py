"""
Objetos
"""


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class ContaCorrente:
    def __init__(self, saldo, limite, cliente: Cliente):
        self.saldo = saldo
        self.limite = limite
        self.cliente = cliente


cliente = Cliente('Higor', '123.456.789-10')
conta_corrente = ContaCorrente(150_000.00, 1_000_000.00, cliente)

print(f'O Cliente: {conta_corrente.cliente.nome} possui {conta_corrente.saldo} reais de saldo e tem um limite '
      f'de {conta_corrente.limite}')

