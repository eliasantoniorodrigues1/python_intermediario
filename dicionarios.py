"""
Dicionários em Python

"""
#
# d1 = {'chave1': 'valor da chave'}
# print(d1)
# # Adicionando um valor ao dicinoário:
# d1['nova_chave'] = 'Valor da nova chave'
# print(d1)
# print(d1['chave1'])
#
# # Outra forma de criar um dicionário
# d2 = dict(chave1='Valor da chave', chave2='Valor da chave2')
# print(d2)
#
# # Forma comumente usada
# d3 = {'chave': 'valor'}
#
# # Você não pode repetir uma chave. Chaves em dicionários precisam ser únicas.
# # Ele sempre irá assumir o valor da última chave igual.
#
# # Para a criação de chaves você pode utilizar qualquer tipo imutável
# d1 = {
#     'str': 'valor',
#     123: 'Outro valor',
#     (1, 2, 3): 'Tupla'
#     }
# print(d1[(1, 2, 3)])
#
# # Se uma chave não existir no dicionário o Python irá levantar uma exceção
# d1['naoexiste'] = 'Agora existe'
# if 'naoexiste' in d1:
#     print(d1['naoexiste'])
# else:
#     print(d1.get('naoexiste'))
#
# print(d1.get('nomedachave'))
#
# # Deletando
# del d1['str']
# print(d1)
#
# # Iterando em um dicionario
# for k, v in d1.items():
#     print(k, v)
#
# # Dicionario dentro de dicionário:
# clientes = {
#     'cliente1': {
#         'nome': 'Luiz',
#         'sobrenome': 'Otávio'
#     },
#     'cliente2': {
#         'nome': 'Elias',
#         'sobrenome': 'Rodrigues'
#     }
# }
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo dados de {clientes_k}: ')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')
#
d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Elias', 'Rodrigues']}
print('Original', d1)
v = d1.copy()
v[1] = 'Elias'
# print(v)
# Se eu tentar alterar o valor dentro da minha lista no dicionário ele irá alterar na cópia e no original
v['d'][0] = 'Zelias'
# print(v)
# Comando pop e pop item no dicionário:
# É necessário dizer o nome da chave
# v.pop(3)
# # Ou popitem para eliminar o ultimo
# v.popitem()
# Para concatenar um dicionário ao outro você utiliza a fução update
c = {'k': 'yyy', 'p': 'xxx'}
d1.update(c)
print('Com o v adicionado', d1)
print('dicionario v', v)