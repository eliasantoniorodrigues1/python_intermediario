"""
Geradores  -

Iteráveis  -

"""
# Iteradores
# lista = [1, 2, 3, 4, 5]
# print(hasattr(lista, '__iter__'))
# lista = iter(lista)
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))


# Geradores
import sys
import time
#
# lista = list(range(1000))
# # Pega a quantidade de bites ocupados na memória.
# print(sys.getsizeof(lista))

# def gera():
#     r = []
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
#
# g = gera()
# print(g)
# for v in g:
#     print(v)

lista1 = [x for x in range(1000)]  # List comprehension
# print(type(lista))
lista2 = (x for x in range(1000))  # Dessa forma transforma a lista em um gerador.
# print(type(lista))
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))

