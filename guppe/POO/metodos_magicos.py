"""
Metodos Magicos -> Todos os métodos que utilizam dunder

dunder init -> __init__()
"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # A funcao desse método é fazer a represtação de um objeto, por default ele retorna o endereço de memória
    def __repr__(self):
        return self.titulo + '__repr__'

    def __str__(self):
        return self.titulo + '__str__'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += str(self) + ' '  # o self é a execuçao do método __str__
            return msg
        return 'Não posso multiplicar'


livro = Livro('Python', 'Some', 400)
print(livro)  # Executa o __repr__, caso nao tenha implementado o __str__ , o __str__ se sobrepoe ao __repr__

print(len(livro))  # Executa o __len__ implementado na classe Livro

del livro  # Executa o __del__ implementado na classe Livro

livro = Livro('Python', 'Some', 400)
livro2 = Livro('Python2', 'Some2', 500)

print(livro + livro2)  # Executa o método __add__
print(livro * 5)  # Executa o método __mul__

# OBS: Ao finalizar a execução do programa, o método del é chamado automaticamente
