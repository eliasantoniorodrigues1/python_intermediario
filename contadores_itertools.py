"""
    Count - Contadores infinitos

"""
from itertools import count

contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break

# Contando invertido
from itertools import count

contador = count(start=-1, step=-1)

for valor in contador:
    print(round(valor, 2))

    if valor <= -10:
        break

# Adicionando índices em uma lista
contador = count()
lista = ['Luiz', 'João', 'Maria', 'José']
lista = zip(contador, lista)
print(list(lista))
