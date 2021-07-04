"""
Escopo de variável

"""
# Escopo Global
variavel = 'valor'

def func():
    print(variavel)


def func2():
    global variavel
    # Variavel criada dentro do escopo local e deixou de ser a variavel global
    variavel = 'Outro valor'
    print(variavel)

func()
func2()
