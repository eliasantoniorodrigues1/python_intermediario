"""
zip
ziplongest - itertools

"""
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BH']

# Se eu quiser unir as duas listas a partir da menor basta usar a função Zip.
# cidade_estado = zip(cidades, estados)  # Nesse momento é criado um gerador

# Agora basta iterar sobre o meu gerador
# for valor in cidade_estado:
#     print(valor)  # Irá imprimir uma tupla que foi unida até a menor lista que no caso é a de estados
                  # e que não tem o estado da cidade de Monte belo

# Se eu quiser unir a partir da maior lista eu tenho que utilizar o Zip_longest
from itertools import zip_longest
# cidade_estado = zip_longest(estados, cidades)
# print(list(cidade_estado))  # Nesse print estou convertendo meu gerador para lista
# Veja que a cidade de Monte Belo não tem estado e nesse caso ficou como None.
# Para resolver esse problema podemos usar o método fillvalues
cidade_estado = zip_longest(estados, cidades, fillvalue='Estado')
print(list(cidade_estado))
