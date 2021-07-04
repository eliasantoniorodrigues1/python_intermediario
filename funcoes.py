"""
    Funções - def em Python

"""
# def saudacao(msg='Olá', nome='usuári'):
#     print(msg, nome)
#
#
# saudacao('Olá mundo!')
# saudacao('Bom dia!')
# saudacao('E aí....')
def saudacao(msg='Olá', nome='usuári'):
    print(msg, nome)
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)
