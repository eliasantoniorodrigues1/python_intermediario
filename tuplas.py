"""
Tuplas
    - São listas imutáveis
"""
# Convertendo tuplas para listas
tupla = (1, 2, 3, 'a', 'Elias Rodrigues')
tupla = list(tupla)
print(type(tupla))

# Você pode criar uma tupla sem os parênteses
t1 = 1, 2, 3, 'a', 'x'
# Você pode fazer concatenação de tuplas
t1 = 1, 2, 3, 4
t2 = 6, 7, 8, 9
t3 = t1 + t2
print(t3)

# Desempacotando uma tupla
n1, n2, *n3, ultimo = t3
print(n1, n2, n3, ultimo)

# Você pode repetir uma tupla  várias vezes apenas usando o sinal de multiplicação:
t1 = t1 * 20
print(t1)
