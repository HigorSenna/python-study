"""
Try, Except, Else, Finally
Else -> é executado somente se não ocorrer erro

"""

try:
    num = int(input('Informe um número'))
    print(f'Você digitou {num}')
except ValueError as err:
    print(f'Numero inválido, erro é: {err}')
else:  # Entra no else se NAO ENTRAR NO EXCEPT
    print('Nao deu erro')
finally:
    print('Executado independente de erro')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel fazer divisão por 0'


def solicitar():

    num1 = input('Informe o primeiro valor: ')
    num2 = input('Informe o segundo valor: ')
    resultado = dividir(num1, num2)

    if type(resultado) is not int and type(resultado) is not float:
        print(resultado)
        print("======================")
        solicitar()
    else:
        print(f'o resultado é: {resultado}')


solicitar()

# Mesmo tratamento para diferentes erros

try:
    error
except(ValueError, ZeroDivisionError, NameError) as err:
    print(f'Ocorreu um problema: {err}')
