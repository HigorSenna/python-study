"""
Forçando tipos de dados com decoradores

"""


def forcar_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forcar_tipo(str, int)
def repetir_mensagem(msg, vezes):
    for vez in range(vezes):
        print(msg)


repetir_mensagem('Teste', 3)
repetir_mensagem('Teste', '3')
