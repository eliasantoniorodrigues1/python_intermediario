"""
04.252.011/0001-10     40.688.134/0001-61  71.506.168/0001-11  12.544.992/0001-05
0425201100011
5 4 3 2 9 8 7 6 5 4 3 2
0 16 6 10 18 0 7 6 0 0 0 2 = 65 ##

Fórmula -> 11 - (65 % 11) = 1
Primeiro Digito = 1

0  4  2  5  2  0  1  1  0  0  0  1  1  x
6  5  4  3  2  9  8  7  6  5  4  3  2
0 20  8  15 4  0  8  7  0  0  0  3  2  = 67 ##

Fórmula -> 11 - (67 % 11) = 11 (Como o resultado é maior que 9, então é 0)
Segundo Dígito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito

"""


def executa_validacao(cnpj):
    return valida_cnpj(trata_cnpj_re(cnpj))


def trata_cnpj(cnpj):
    return cnpj.replace('.', '').replace('/', '').replace('-', '')


def trata_cnpj_re(cnpj):
    import re
    return re.sub(r'[^0-9]', '', cnpj)

def sequencia(cnpj):
    


def valida_cnpj(cnpj):
    contador = 5
    soma = indice = 0
    novo_cnpj = cnpj[0:12]
    for i in range(0, 25):
        posicao = int(novo_cnpj[indice])
        soma += contador * posicao
        contador -= 1

        if contador < 2:
            contador = 9

        if i == 11:
            digito_1 = 11 - (soma % 11)
            novo_cnpj += str(digito_1)
            contador = 6
            soma = indice = 0
            continue

        if i == 24:
            digito_2 = 11 - (soma % 11)
            if digito_2 > 9:
                digito_2 = 0
                novo_cnpj += str(digito_2)
            else:
                digito_2 = str(digito_2)
                novo_cnpj += str(digito_2)

        indice += 1
    if novo_cnpj == cnpj.replace('.', '').replace('/', '').replace('-', ''):
        return f'CNPJ Válido'
    else:
        return f'CNPJ inválido'


if __name__ == '__main__':
    # 40.688.134/0001-61  71.506.168/0001-11  12.544.992/0001-05  04.252.011/0001-10
    cnpj = '04.252.011/0001-10'
    print(executa_validacao(cnpj))
