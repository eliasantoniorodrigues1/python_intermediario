"""
Dictionary Comprehension

"""
# lista = [
#     ('chave', 2),
#     ('chave2', 'valor2'),
#     ]
#
# d1 = {x: y*2 for x, y in lista}
# print(d1)

# Pode utilizar para criar set também (Compreenção de conjuntos
# d1 = {x for x in range(5)}
# print(d1, type(d1))

# Criando um dicioário utilizando o Range()
d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)