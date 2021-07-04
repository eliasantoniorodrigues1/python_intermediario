"""
Funções (def) em Python - *args **kwargs
Se você setar um valor padrão para algum argumento da função, todos que vierem após
deverá ter um valor padrão.
A partir do momento que você chama uma função com argumento nomeado, você não pode mais
chamar sem nomear.
"""
# def func(*args, **kwargs): # Keyword args
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#     # Converter tupla em lista:
#     args = list(args)

lista = [1, 2, 3, 4, 5]
# Desempacotando os dois primeiros valores e empacotando o restante da lista
n1, n2, *n = lista
# print(n1, n2, n)
# É como se você estivesse fazendo o print abaixo:
# print(*lista) # Desempacotando a lista
# func(1, 2, 3, 4, 5)

# Você envia uma lista desempacotada para evitar confusão dentro da função
# pois ao gerar a tupla os índices irão ficar em ordem, do contratrário o primeiro elemento
# da tupla vai ser uma lista.
# lista = [1, 2, 3, 4]
# func(*lista)

# Argumentos com palavra chaves: **kwargs
def funcao(*args, **kwargs):
    print(args)
    print(kwargs) # Desempacotou meus argumentos nomeados!
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')  # MELHOR FORMA DE USO!
    if idade is not None:
        print('Idade não enviada.')


lista2 = [1, 2, 3, 4, 5]
funcao(*lista2, nome='Elias', sobrenome='Rodrigues')
