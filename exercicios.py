# 1 – Crie uma função que exibe uma saudação com os parâmetros saudação e nome.

# def saudacao(msg='Olá', nome='usuário'):
#     return f'{msg} {nome}'
#
# variavel = saudacao(nome='Elias')
# print(variavel)


# 2 – Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
#
#
# def soma(n1, n2, n3):
#     return n1 + n2 + n3
#
#
# total = soma(5, 5, 5)
# print(total)


# 3 – Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%).
# Retorne o valor do primeiro número somado do aumento do percentual do mesmo.



# def aumento(valor, percent):
#     tot = (1 + (percent / 100)) * valor
#     return tot
#
#
# def valida_numero(n):
#     try:
#         n = float(n)
#         return n
#     except:
#         return False
#
#
# while True:
#     valor = valida_numero(input('Digite um valor: R$'))
#     percentual = valida_numero(input('Digite um percentual: '))
#     if not valor:
#         print('Valor inválido.')
#     elif not percentual:
#         print('Percentual inválido.')
#     else:
#         break
# total = aumento(valor, percentual)
# print(f'{percentual}% de aumento sob R${valor:.2f} dá um total de: R${total:.2f}')

# percentual = input('Digite um percentual (apenas números inteiros): ')

# tot_aumento = aumento(valor, percentual)
# print(f'Aumentando {percentual}% em {valor}, temos R${tot_aumento}')


# 4 – Fizz Buzz – Se o parâmetro da função for divisível por 3, retorne fizz,
# se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função
# for divisível por 5 e 3, retorne FizzBuzz, caso contrário, retorne o número enviado.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n


def valida_numero(n):
    try:
        n = int(n)
        n = fizzbuzz(n)
    except:
        return f'O número digitado é inválido.'

    return n


n = input('Digite um número: ')
resp = valida_numero(n)
print(resp)
