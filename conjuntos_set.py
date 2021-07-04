"""
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

"""
# s1 = {1, 2, 3, 4, 5, 6}
# for v in s1:
#     print(v)
#
# # Adicionando valores no set
# s1.add((1, 2, 3, 'Elias'))
# print(s1)
#
# # Remover um valor
# s1.discard(2)
#
# # Atualizar um valor
# s1.update('Python')  # Recebe um iterável muito usada com lista, ou com outro set
# print(s1)
# # Sets não respeitam ordem
#
# # Não aceita elementos duplicados, em caso de você passar dois iguais, ele irá manter somente um.
#
# # É muito utilizado para eliminar elementos duplicados em uma lista:
# li = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 6, 'Elias', 'Elias']
# li = set(li)
# print(li)

# Union
# x1 = {1, 2, 3, 4, 5}
# x2 = {1, 2, 3, 4, 5, 6}
# # x3 = x1 | x2
# # print(x3)
# # x3 = union(x1, x2
#
# # Intersection - Elementos presentes nos dois sets
# x3 = x1 & x2
# print(x3)

# Pegar a diferença de dois sets
# Mostra somente o elemento que está em apenas um dos sets, levando sempre em consideração o
# set da esquerda.
# x1 = {1, 2, 3, 4, 5, 7}
# x2 = {1, 2, 3, 4, 5, 6}
# x3 = x1 - x2  # Irá retornar o elemento 6, pois é único no set da esquerda.
# print(x3)

# Pega somente os elementos que são únicos em cada elemento
# x1 = {1, 2, 3, 4, 5, 7}
# x2 = {1, 2, 3, 4, 5, 6}
# x3 = x1 ^ x2
# print(x3)

# Outras formas de usar
l1 = ['Luiz', 'João', 'Maria']
l2 = ['João', 'Maria', 'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Luiz']
# Você pode testar se uma lista é igual a outra mesmo tendo elementos duplicados
l1 = set(l1)
l2 = set(l2)
print(l1 == l2)
