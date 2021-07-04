"""
List Comprehesion

"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Declarando uma variável e iterando a lista
l2 = [variavel for variavel in l1]

# Executando uma multiplicação dentro dos elementos da l1
ex3 = [variavel * 2 for variavel in l1]

# usando if dentro da list comprehension

ex4 = [variavel for variavel in l1 if variavel % 8 == 0]
# print(ex4)  # Imprimiu somente o multiplo de 8 dentro da lista

# Exemplo com if composto

l1 = list(range(100))  # Criando uma lista com um range de 0 a 99
# print(l1)

# Condição composta
ex5 = [variavel if variavel % 3 == 0 and variavel % 8 == 0 else 0 for variavel in l1]
# print(ex5)

# Criando uma Tupla com o formato de coordenada
ex6 = [(x, y) for x in l1 for y in range(3)]
print(ex6)


