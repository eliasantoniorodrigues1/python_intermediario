# 1 - Crie uma função que recebe uma função como parâmetro e retorne o valor
# da função2 executada.

def irrf(liquido):
    liquido += (liquido * -0.07)
    return liquido


def inss(sal):
    sal += (sal * -0.10)
    return irrf(sal)


print(inss(1000))

# 2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
# Faça a função 1 executar duas funções que recebam um número diferente de argumentos.


def usuario(arg):
    return arg


def saudacao(*args,  **kwargs):
    return args, kwargs


# Resolulção do Professor
# 1 - Exercicio 1

def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):  # Esse argumento função se torna a função ola_mundo()
    return funcao()


executando = mestre(ola_mundo)  # Nessa parte ele chama a funçã ola_mundo sem executar, porque não tem
                                # parênteses, quem vai executar ela é a função mestre().


print(executando)

# 2 - Exercicio 2
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Elias')
executando2 = mestre(saudacao, 'Elias', saudacao='Boa tarde!')
print(executando)
print(executando2)

# Eu posso ter uma função mestre que chama o calculo uma função qualquer, com *args e **kwargs
# Dentro da função mestre eu posso validar por exemplo se o cara digitou número de dependentes para
# calcular o imposto de renda com o comando numero_dependente = args.get('dependente')
