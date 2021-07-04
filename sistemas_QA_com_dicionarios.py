"""
Sistema de Perguntas e Respostas com Dicionários:

"""
qtd_acertos = 0
perguntas = {
    'Pergunta 1': {'pergunta': 'Quanto é 2 + 2?', 'respostas': {'a': 1, 'b': 5, 'c': 4}, 'resposta_certa': 'c'},
    'Pergunta 2': {'pergunta': 'Quanto é 1 + 1?', 'respostas': {'a': 1, 'b': 2, 'c': 4}, 'resposta_certa': 'b'},
    'Pergunta 3': {'pergunta': 'Quanto é 2 - 5?', 'respostas': {'a': -3, 'b': 5, 'c': 4}, 'resposta_certa': 'a'},
    'Pergunta 4': {'pergunta': 'Quanto é 5 * 2?', 'respostas': {'a': 1, 'b': 10, 'c': 15}, 'resposta_certa': 'b'},
    'Pergunta 5': {'pergunta': 'Quanto é 9 * 9?', 'respostas': {'a': 81, 'b': 5, 'c': 4}, 'resposta_certa': 'a'},
            }
# Loop para percorrer cada pergunta e suas respectivas opções.
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] {rv}')
    resp = input('Sua resposta: ')
    if resp == pv['resposta_certa']:
        qtd_acertos += 1
print()
# ==============================================
tot_perguntas = len(perguntas)
percentual = (qtd_acertos / tot_perguntas) * 100
# Exibição do resultado
print(f'Você acertou {qtd_acertos} respostas.')
print(f'Seu percentual de acerto foi de {percentual:.2f}%')
