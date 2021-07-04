"""
01 - Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação.
Retorne a duplicação considerada.
Requisitos: A ordem do número duplicado é considerada a partir da segunda ocorrência do número,
ou seja, o número duplicado em si.

Exemplo:
[1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são suplicados (retorne 3)
[1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados

"""


lista_numeros_interios = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 1, 1, 2, 5, 6],
    [10, 9, 8, 7, 5, 6, 4, 1],

]



def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()  # Cria um set vazio, pois sets não aceitam duplicados
    primeiro_duplicado = -1  # Define a variavel de retorno já como -1, em caso de não achar duplicados.

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero  # Se o número atual já estiver dentro do set quer dizer que ele é duplic.
            break   # Quebra o laço, pois já encontrou o primeiro duplicado.

        numeros_checados.add(numero)  # Do contrário vai adicionando os números no set, até encontrar o primeiro duplicado.

    return primeiro_duplicado



for lista_inteiros in lista_numeros_interios:
    print(lista_inteiros, encontra_primeiro_duplicado(lista_inteiros))
