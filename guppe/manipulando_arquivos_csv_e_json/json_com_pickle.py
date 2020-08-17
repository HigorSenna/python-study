"""
Trabalhando com JSON + Pickle

pip install jsonpickle
"""

import json
import jsonpickle


class Cachorro:
    def __init__(self, nome):
        self.__nome = nome

    def latir(self):
        print(f'{self.nome} está latindo')

    @property
    def nome(self):
        return self.__nome


cachorro = Cachorro('Pluto')

json_string = json.dumps(['produto', {'Playstation4': ('2TB', 'Novo', '220V')}])
print(json_string)

cachorro_json = json.dumps(cachorro.__dict__)
print(cachorro_json)


# JSON PICKLE
ret = jsonpickle.encode(cachorro)
print(ret)

# Escrevendo com JSON PICKLE
with open('cachorro.json', 'w') as arquivo:
    ret = jsonpickle.encode(cachorro)
    arquivo.write(ret)

# Lendo com JSON PICKLE

with open('cachorro.json', 'r') as arquivo:
    conteudo = arquivo.read()
    cachorro_by_json: Cachorro = jsonpickle.decode(conteudo)
    print(cachorro_by_json.nome)