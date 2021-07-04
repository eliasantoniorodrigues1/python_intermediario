# https://docs.python.org/3/library/functions.html#open
# Exemplo salvar as configurações do seu sistema em um dicionário
# Salvar em um arquivo jason, depois converter para um dicionário novamente para fazer a leitura do dicionário.

# file = open('abc.txt', 'w+')
#
# # Escrita
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# # Leitura do arquivo inteiro
# # Toda vez que você cria uma linha em um arquivo em Python, o mesmo utiliza o cursor para se localizar
# # dentro do arquivo, porém ao criar uma linha o cursor estará posicionado no final da linha e se você utilizar
# # o comando read() ele vai ler a partir de onde o cursor está, não exibindo nada na tela.
# print('Não leu nada')
# print(file.read())
# print('Lendo linhas')
# file.seek(0, 0)
# print(file.read())
# # Sempre voltar o cursor para o inicio do arquivo
# file.seek(0, 0)
#
# # Exibindo as linhas usando o readline()
# print('Lendo linha a linha')
# print(file.readline(), end='')  # Irá ler a primeira linha
# print(file.readline(), end='')  # Irá ler a segunda linha
#
# # Exibindo todas as linhas em uma lista
# file.seek(0, 0)
# print('Linhas em lista')
# print(file.readlines())
# # Você pode fazer um for dentro do readlines() já que ele joga os dados em uma lista.

# file.close()

# Forma Pythonica de abrir arquivos
# Utilizando gerenciador de contextos "with":
# Nesse módulo de gerenciador de contexto não é necessário solicitar para fechar o arquivo
# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0, 0)
#     print(file.read(), end='')

# Somente leitura
# with open('abc.txt', 'r') as file:
#     print(file.read())
#
# # Abre no modo append
# with open('abc.txt', 'a+') as file:
#     file.write('Outra linha\n')
#     file.seek(0, 0)
#     print(file.read())
#
# # Apagar arquivo
# import os
# os.remove('abc.txt')

# Convertendo o arquivo para jason
import json
d1 = {
    'Pessoa1': {
        'nome': 'Elias',
        'idade': 33,
    },
    'Pessoa2': {
        'nome': 'Ana',
        'idade': 27,
    },
}
d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
print(d1_json)

