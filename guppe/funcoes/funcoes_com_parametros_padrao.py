"""
Funcoes com parametros padrao

Ordem de declarção de parâmetros:

 1 - Parâmetros obrigatorios
 2 - Parâmetros default

"""

# Default param


def exponcencial(numero, potencia=2):
    return numero ** potencia


print(exponcencial(2))
print(exponcencial(2, 3))

# Funcoes como parametro default


def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def realizar_operacao(num1, num2, funcao=somar):
    return funcao(num1, num2)


print(realizar_operacao(5, 3))
print(realizar_operacao(5, 3, subtrair))

# Escopo

instrutor = 'Teste'  # Se puder evitar, evite as variaveis globais


def dizer_oi():
    instrutor = 'Testando'  # Se tivermos uma variavel local com o mesmo nome da global, a local prevalece no metodo
    return f'Oi {instrutor}'


def dizer_oi_usando_variavel_global():
    global instrutor
    instrutor = 'Testando'
    return f'Oi {instrutor}'


# Podemos ter funções que são declaradas dentro de funções (Não é comum)


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())
