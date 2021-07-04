"""
Agrupando elementos em dicionário em Python
"""
from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Elias', 'nota': 'A'},
    {'nome': 'Camila', 'nota': 'B'},
    {'nome': 'Ferreira', 'nota': 'C'},
    {'nome': 'Lucas', 'nota': 'D'},
    {'nome': 'Reginal', 'nota': 'B'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Luiza', 'nota': 'A'},
    {'nome': 'Cornélio', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'E'},
    {'nome': 'João', 'nota': 'A'},
]

# Para que o groupby funcione o dicionário precisa estar ordenado
# Para ordenar um dicionário utilizamos a função sort + uma expressão lambda como chave:
ordem = lambda item: item['nota']
alunos.sort(key=ordem)
alunos_agrupados = groupby(alunos, key=ordem)
# for dado in alunos_agrupados:
#     print(f'Agrupamento {dado[0]}:')
#     for lista in dado[1]:
#         print(f'\t{lista["nome"]}')

# Fazer um for desempacotando o item agrupado A, B, C, D, E e a lista em variáveis diferentes:
for agrupamento, valores_agrupado in alunos_agrupados:
    print(f'Agrupamento de {agrupamento}:')
    quantidade = len(list(valores_agrupado))  # valores_agrupados é um iterador e se você utilizar o for após, ele já terá se esgotado.
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
