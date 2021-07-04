"""
01 - Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação.
Retorne a duplicação considerada.
Requisitos: A ordem do número duplicado é considerada a partir da segunda ocorrência do número,
ou seja, o número duplicado em si.

Exemplo:
[1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são suplicados (retorne 3)
[1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados

"""


def duplicado(lista):
    sem_duplicados = list(set(lista))
    fim = 0
    contador = 0
    flag = len(lista)
    while contador < flag:

        for i in lista[:contador + 1]:
            if contador == 0:
                continue

            atual = lista[contador]
            anterior = lista[contador - 1]

            if atual == anterior:
              return atual

        contador += 1
        if contador >= flag:
            return f'-1 (não tem valor repetido)'


if __name__ == '__main__':
    print(duplicado([1, 2, 3, 3, 2, 1]))
    print(duplicado([1, 2, 3]))
    print(duplicado([1, 2, 3, 4, 5, 6, 7]))
    print(duplicado([1, 1, 2, 2, 3, 4, 5, 6, 7]))
    print(duplicado([1, 2, 3, 4, 5, 6, 7, 7, 7, 1]))

