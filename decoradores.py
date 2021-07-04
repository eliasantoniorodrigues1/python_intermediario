# Eu posso atribuir uma função a uma variável e essa variável vai se comportar
# como uma função.
# def fala_oi():
#     print('Oi')
#
#
# variavel = fala_oi
#
# variavel()

def master():
    def slave():
        print('oi')
    return slave

# @master
variavel = master()
variavel()
