import os
import re
from shutil import move

def move_arquivos(caminho):
    contador = 0
    for root, dir, files in os.walk(caminho):
        # print(root, dir, files)
        for file in files:
            valida = valida_arquivos_py(file)
            if valida:
                caminho_arquivo = f'{root}\\{file}'
                # print(f'Mover de "{caminho_arquivo}" para "{caminho}"')
                try:
                    # print(f'{caminho_arquivo}\t\t {destino}')
                    move(caminho_arquivo, destino)
                except Exception as erro:
                    print(file, erro.__class__)
                


def valida_arquivos_py(extensao):
    regexp = re.compile(r'^[a-zA-Z]+.*\.py$')
    if regexp.findall(extensao):
        return True
    else:
        return False


if __name__=='__main__':
    # Implementar para ele mover exceto ele mesmo....
    caminho = 'D:\\Cursos\\Luiz_Otavio_Miranda\\Python\\Intermediario'
    destino = 'D:\\Cursos\\arquivos'
    print('Movendo arquivos...')
    move_arquivos(caminho)
    print('Caminho dos arquivos alterado com sucesso!')