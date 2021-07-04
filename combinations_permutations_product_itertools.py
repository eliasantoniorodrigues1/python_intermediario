"""
Combinations - Permutations - Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos

"""
from itertools import combinations, permutations, product

# Quando a ordem NÃO importar você pode utilizar o combinations
pessoa = ['Elias', 'Luiz', 'André', 'Eduardo', 'Letícia', 'Fabricio', 'Rose']
for grupo in combinations(pessoa, 2):
    print(grupo)

print('#' * 30)
# Quando a ordem importar você pode utilizar o permutations
for grupo in permutations(pessoa, 2):
    print(grupo)
print('#' * 30)
# Para pegar todas as combinações possíveis utiliza-se o Product
for grupo in product(pessoa, repeat=2):
    print(grupo)
