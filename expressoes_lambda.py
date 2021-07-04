"""
Funções anônimas - Expressões Lambda

"""
a = lambda x, y: x * y
print(a(2, 2))

# Muito utilizado para passar uma função como parâmetro
# Exemplo: Ordernar a lista abaixo, para fazer isso seria necessário criar uma função e passar ela como
# arumento para o comando sort(key=nome_funcao) e dentro da minha funcao eu passaria o indice que quero ordenar
# no exemplo abaixo seria 1, porque quero ordernar pelo valor.
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 3],
    ['P4', 7],
    ['P5', 50]

]

def ordena(item):
    return item[1]

lista.sort(key=ordena, reverse=True)
print(lista)

# Usando a função anônima ficaria conforme abaixo:
lista.sort(key=lambda item: item[1])
print(lista)

# Usando a funcao sorted
print(lista.sorte(key=lambda i: i[1], reverse=True))
