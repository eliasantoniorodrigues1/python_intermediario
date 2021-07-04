"""
    Função Map no Python
    A função map recebe uma função como primeiro argumento. Normalmente utilizamos uma expressão lambda.
    Ela retorna um iterador e não uma lista.
    Geralmente é melhor utilizar a função map com dicionário
"""
from dados import produtos, pessoas, lista

# Mapeando dados para modificá-los
# Suponha ser necessário multiplicar cada elemento da lista

# nova_lista = map(lambda x: x * 2, lista)
#
# print(lista)
# print(list(nova_lista))  # A funão map() retorna um iterador, que pode ser convertido
#                          # em uma lista.
#

# Suponha que eu precise aumentar 5% em cada um dos preços do
# dicionário, podemos fazer de várias formas, mas iremos fazer com map()

# for produto in produtos:
#     print(produto)

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
# # Criar um novo dicionário contendo somente os precos
# # precos = map(lambda p: p['preco'], produtos)
# novos_produtos = map(aumenta_preco, produtos)
# for preco in novos_produtos:
#     print(preco)

def aumenta_idade(p):
    p['nova_idade'] = int(p['idade'] * 1.20)
    return p  # Nesse caso estou criando um novo campo dentro do meu dicionário

# Criar uma nova lista contendo somente os nomes do dicionário
# nomes = map(lambda p: p['nome'], pessoas)
idade = map(aumenta_idade, pessoas)

for pessoa in idade:
    print(pessoa)

