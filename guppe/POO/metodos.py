"""
Metodos

OBS: Os métodos/funções dunder(__) em python são chamados de métodos mágicos:

__init__, __main__.. etc

Para ser chamados de dunder, deve iniciar com __ e terminar com __

__nome -> náo é dunder nome

__init__ -> é chamado de dunder init

Em Python

Metodos de instancia -> trabalha com os atributos do objeto
Metodo de classe(@classmethod) -> trabalha com os atributos da classe
Metodo statico (@staticmethod) -> Nao usa nada da classe e nem do objeto

"""


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email

    # Nao é recomendado que nós desenvolvedores criamos métodos com dunder, pois podemos eventualmente causar confsao
    # e até mesmo criar um método dunder nosso que já exista no python
    def __correr__(self, metros):
        print(f'{self.nome} correndo {metros} metros')


class Produto:
    contador = 0

    def __init__(self, nome, valor):
        self.__id = Produto.contador + 1
        self.nome = nome
        self.__valor = valor
        Produto.contador = self.__id

    @property
    def valor(self):
        return self.__valor

    def aplicar_desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        if self.__valor > 0:
            return (self.__valor * (100 - porcentagem)) / 100
        return self.__valor


produto = Produto('PS5', 6000)
msg = f'O Produto: {produto.nome} sai de: {produto.valor} por {produto.aplicar_desconto(30)}'
print(msg)
print(Produto.aplicar_desconto(produto, 20))  # Outra forma de chamar métodos de instancia


# Criptografando
# pip install passlib

from passlib.hash import pbkdf2_sha256 as cryp


class Credencial:
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = cryp.hash(senha)

    def e_senha_valida(self, senha):
        return cryp.verify(senha, self.__senha)


credencial = Credencial('email@gmail.com', '123456')

print(credencial._Credencial__senha)
print(credencial.e_senha_valida('123456'))

# Metodos de Classe (em Java: métodos statics)


class CredencialUsuario:

    contador = 0

    @classmethod
    def contar_usuarios(cls):
        print(f'Temos {cls.contador} usuario(s) logado(s) no sistema')

    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = cryp.hash(senha)
        CredencialUsuario.contador += 1

    def e_senha_valida(self, senha):
        return cryp.verify(senha, self.__senha)


c1 = CredencialUsuario('abc@gmail.com', '123456')
c2 = CredencialUsuario('abccc@gmail.com', '123456')
c3 = CredencialUsuario('acxcbc@gmail.com', '123456')
c4 = CredencialUsuario('abccc@gmail.com', '123456')

CredencialUsuario.contar_usuarios()  # forma correta
c1.contar_usuarios()  # Possível, mas incorreto


# Metodos Estáticos

class CredencialUsuarioSistema:

    contador = 0

    @staticmethod
    def ver():
        print('Vendo')

    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = cryp.hash(senha)
        CredencialUsuario.contador += 1

    def e_senha_valida(self, senha):
        return cryp.verify(senha, self.__senha)


CredencialUsuarioSistema.ver()
