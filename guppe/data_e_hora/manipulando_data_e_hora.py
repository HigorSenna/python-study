"""
Manipulando Data e Hora


"""

import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now())

data = datetime.datetime.now()
print(data)
data = data.replace(hour=16, minute=0, second=0, microsecond=0)
print(data)

evento = datetime.datetime(2019, 1, 1, 0)
print(evento)
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)