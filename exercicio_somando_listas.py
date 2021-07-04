"""
Faça a soma de duas listas em uma terceira lista usando list comprehension.
lista1 = [1, 2, 3, 4, 5, 6, 7 , 8]
lista2 = [1, 2, 3, 4]
lista3 = [2, 4, 6, 8]
"""
lista1 = [1, 2, 3, 4, 5, 6, 7 , 8]
lista2 = [1, 2, 3, 4]
# lista3 = [sum((x, y)) for x, y in list(zip(lista1, lista2))]
# print(lista3)

# from itertools import zip_longest
# lista3 = zip_longest(lista1, lista2, fillvalue=0)  # 1º Crio uma lista unificada
# lista3 = list(zip_longest(lista1, lista2, fillvalue=0))  # 2º Trasformo meu gerador em lista
# lista3 = [sum((x, y)) for x, y in lista3]  # Faço um list comprehension somando cada tupla, dessa forma terei uma lista com a soma dos valores
# print(list(lista3))


# Resolução do Professor:
# Funciona em qualquer linguagem
# lista_soma = []
# for i in range(len(lista2)):
#     lista_soma.append(lista1[i] + lista2[i])
# print(lista_soma)

# Jeito um pouco mais Pythonico
# lista_soma = []
# for i, _ in enumerate(lista2):
#      lista_soma.append(lista1[i] + lista2[i])
# print(lista_soma)

# Usando List Comprehension
lista_soma = [x + y for x, y in zip(lista1, lista2)]
print(lista_soma)
